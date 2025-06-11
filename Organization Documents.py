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
        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1][1:].lower()

            if destination_root in file_path or programming_folder in file_path or office_folder in file_path:
                continue

            if file_extension in programming_extensions:
                dest_subfolder = os.path.join(programming_folder, programming_extensions[file_extension])
                os.makedirs(dest_subfolder, exist_ok=True)
                destination_path = os.path.join(dest_subfolder, filename)
                shutil.move(file_path, destination_path)
                print(f"Movido para Programação: {file_path} -> {destination_path}")

            elif file_extension in office_extensions:
                dest_subfolder = os.path.join(office_folder, office_extensions[file_extension])
                os.makedirs(dest_subfolder, exist_ok=True)
                destination_path = os.path.join(dest_subfolder, filename)
                shutil.move(file_path, destination_path)
                print(f"Movido para Documentos: {file_path} -> {destination_path}")

            elif file_extension in common_extensions:
                dest_subfolder = os.path.join(destination_root, common_extensions[file_extension])
                os.makedirs(dest_subfolder, exist_ok=True)
                destination_path = os.path.join(dest_subfolder, filename)
                shutil.move(file_path, destination_path)
                print(f"Movido para Geral: {file_path} -> {destination_path}")

            else:
                dest_subfolder = os.path.join(destination_root, "Outros")
                os.makedirs(dest_subfolder, exist_ok=True)
                destination_path = os.path.join(dest_subfolder, filename)
                shutil.move(file_path, destination_path)
                print(f"Movido para Outros: {file_path} -> {destination_path}")

    print("Organização completa! Todos os arquivos foram movidos para as pastas apropriadas.")


organizar_arquivos(source_folder, destination_root, programming_folder, office_folder)
