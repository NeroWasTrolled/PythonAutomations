import re

txt_input_file = 'C:/Users/gabriel.simoes/Documents/Teste/arquivo.txt'
txt_output_file = 'C:/Users/gabriel.simoes/Documents/Teste/conversao.txt'

try:
    with open(txt_input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts_pattern = r'"parts":\s*\[\s*"([^"]*)"\s*\]'
    parts_matches = re.findall(parts_pattern, content)
    
    with open(txt_output_file, 'w', encoding='utf-8') as f:
        for part in parts_matches:
            f.write(part + "\n")  
    
    print(f"Conteúdo de 'parts' foi salvo com sucesso em '{txt_output_file}'.")

except FileNotFoundError:
    print(f"O arquivo '{txt_input_file}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
