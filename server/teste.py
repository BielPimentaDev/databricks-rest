import pandas as pd
import json

"[UNRESOLVED_COLUMN.WITH_SUGGESTION]"
"SQLSTATE: 42703"
json_file = 'relatorios.json' 

def traduzir_erro(erro):
    if "IndexError: list index out of range" in erro:
        return "Falta de arquivo correspondente"
    elif erro.startswith("[UNRESOLVED_COLUMN.WITHOUT_SUGGESTION]"):
        return erro.replace("[UNRESOLVED_COLUMN.WITHOUT_SUGGESTION]", "").strip()
    elif erro.startswith("[UNRESOLVED_COLUMN.WITH_SUGGESTION]"):
        return erro.replace("[UNRESOLVED_COLUMN.WITH_SUGGESTION]", "").strip()
    
    return erro.replace("SQLSTATE: 42703", "").strip()  

with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)


rows = []

for item in data:
    mes = item['mes']
    for fundo in item['fundos']:
        for batimento in fundo['batimentos']:
            erro_traduzido = traduzir_erro(batimento['erro'])
            rows.append({
                'mes': mes,
                'fundo': fundo['fundo'],
                'batimento': batimento['batimento'],
                'erro': erro_traduzido
            })



df = pd.DataFrame(rows)


excel_file = 'seu_arquivo.xlsx'  
df.to_excel(excel_file, index=False)

print(f"Arquivo Excel '{excel_file}' criado com sucesso!")