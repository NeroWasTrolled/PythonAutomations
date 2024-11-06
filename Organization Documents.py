import os
import shutil
from datetime import datetime
from collections import Counter

source_folder = ''
destination_root = ''
programming_folder = ''
office_folder = ''

programming_extensions = {
    'py': 'Python',
    'cs': 'C#',
    'java': 'Java',
    'js': 'JavaScript',
    'html': 'HTML',
    'css': 'CSS',
}

office_extensions = {
    'doc': 'Word',
    'docx': 'Word',
    'xls': 'Excel',
    'xlsx': 'Excel',
    'ppt': 'PowerPoint',
    'pptx': 'PowerPoint',
}

common_extensions = {
    'txt': 'TXT',
    'pdf': 'PDF',
    'png': 'Imagens',
    'jpeg': 'Imagens',
    'jpg': 'Imagens',
    'gif': 'Imagens',
    'zip': 'Compactados',
    'json': 'JSON',
}

def organizar_arquivos(source_folder, destination_root, programming_folder, office_folder):
    for root, dirs, files in os.walk(source_folder):
        file_extensions = [os.path.splitext(filename)[1][1:].lower() for filename in files]

        programming_files = [ext for ext in file_extensions if ext in programming_extensions]
        if programming_files:
            extension_count = Counter(programming_files)
            dominant_extension = extension_count.most_common(1)[0][0]

            if len(programming_files) > 1:
                project_folder = os.path.join(programming_folder, programming_extensions[dominant_extension])
                os.makedirs(project_folder, exist_ok=True)

                project_destination = os.path.join(project_folder, os.path.basename(root))
                shutil.move(root, project_destination)
                print(f"Projeto movido: {root} -> {project_destination}")
                continue

        office_files = [ext for ext in file_extensions if ext in office_extensions]
        if office_files:
            for filename in files:
                file_path = os.path.join(root, filename)
                if destination_root in file_path:
                    continue

                file_extension = os.path.splitext(filename)[1][1:].lower()
                if file_extension in office_extensions:
                    office_subfolder = os.path.join(office_folder, office_extensions[file_extension])
                    os.makedirs(office_subfolder, exist_ok=True)

                    destination_path = os.path.join(office_subfolder, filename)
                    shutil.move(file_path, destination_path)
                    print(f"Movido para Office: {file_path} -> {destination_path}")

            continue

        for filename in files:
            file_path = os.path.join(root, filename)
            if destination_root in file_path:
                continue

            file_extension = os.path.splitext(filename)[1][1:].lower()
            if file_extension in common_extensions:
                destination_folder = os.path.join(destination_root, common_extensions[file_extension])
            else:
                destination_folder = os.path.join(destination_root, "Outros")

            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Movido: {file_path} -> {destination_path}")

    print("Organização completa! Todos os arquivos foram movidos para as pastas apropriadas.")

organizar_arquivos(source_folder, destination_root, programming_folder, office_folder)
