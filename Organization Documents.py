import os
import shutil
from datetime import datetime

source_folder = ''  
destination_root = '' 

def organizar_arquivos(source_folder, destination_root):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)

            if destination_root in file_path:
                continue

            file_creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(file_creation_time)
            year = creation_date.strftime('%Y')
            month = creation_date.strftime('%B') 

            file_extension = os.path.splitext(filename)[1][1:] 
            if not file_extension: 
                file_extension = "Outros"  

            destination_folder = os.path.join(destination_root, year, month, file_extension.upper())

            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Movido: {file_path} -> {destination_path}")

    print("Organização completa! Todos os arquivos foram movidos para a pasta centralizada.")

organizar_arquivos(source_folder, destination_root)
