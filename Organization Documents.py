import os
import shutil
from datetime import datetime

# Pasta raiz onde os arquivos estão espalhados (ex: Downloads)
source_folder = 'C:/Users/gabriel.simoes/Downloads'  # Substitua pelo caminho da pasta raiz
# Pasta de destino centralizada onde os arquivos organizados serão armazenados
destination_root = 'C:/Users/gabriel.simoes/Documents/ArquivosParaOrganizar'  # Substitua pelo caminho da pasta de destino

def organizar_arquivos(source_folder, destination_root):
    # Itera sobre todos os arquivos e subpastas na pasta raiz
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            # Obtem o caminho completo do arquivo atual
            file_path = os.path.join(root, filename)

            # Ignora se o arquivo já está na pasta de destino
            if destination_root in file_path:
                continue

            # Obtém a data de criação do arquivo
            file_creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(file_creation_time)
            year = creation_date.strftime('%Y')
            month = creation_date.strftime('%B')  # Nome do mês (ex: Janeiro, Fevereiro)

            # Extrai a extensão do arquivo
            file_extension = os.path.splitext(filename)[1][1:]  # Remove o ponto da extensão
            if not file_extension:  # Ignora arquivos sem extensão
                file_extension = "Outros"  # Define uma pasta 'Outros' para arquivos sem extensão

            # Define o caminho da pasta de destino baseada em ano, mês e extensão
            destination_folder = os.path.join(destination_root, year, month, file_extension.upper())

            # Cria a pasta de destino se ela ainda não existir
            os.makedirs(destination_folder, exist_ok=True)

            # Move o arquivo para a pasta de destino
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Movido: {file_path} -> {destination_path}")

    print("Organização completa! Todos os arquivos foram movidos para a pasta centralizada.")

# Chama a função para organizar os arquivos
organizar_arquivos(source_folder, destination_root)
