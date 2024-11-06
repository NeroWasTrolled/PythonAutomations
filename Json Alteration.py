import json

json_file = ''
txt_file = ''   

try:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f) 

    with open(txt_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Dados do arquivo JSON '{json_file}' foram salvos com sucesso em '{txt_file}'.")

except FileNotFoundError:
    print(f"O arquivo '{json_file}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"O arquivo '{json_file}' não está em um formato JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
