import requests
import json

url = 'https://adb-3694987222772985.5.azuredatabricks.net/api/2.1/jobs/list'

token = 'dapi0623242a7e6f05190933214f08f250f5-3'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}



def limpar_nome(nome):
    nome_normalizado = unicodedata.normalize('NFD', nome)
    nome_sem_acento = ''.join(c for c in nome_normalizado if not unicodedata.combining(c))
    nome_limpo = nome_sem_acento.replace(' ', '_')
    return nome_limpo



def process_fundos():
    tasks = []
    for i, fundo in enumerate(FUNDS):
        task = {
      "task_key": limpar_nome(fundo),
      "run_job_task": {
        "job_parameters": {
          "fundo": fundo
        },
        "job_id": "539449877491210"
      },
      "timeout_seconds": 3600
    }
        tasks.append(task)
        
    job_config = {"name": "BATIMENTOS",
        "run_name": "BATIMENTOS",
        "access_control_list": [
            {
            "user_name": "zalmom.silva@pwc.com",
            "permission_level": "CAN_MANAGE_RUN"
            },
            {
            "user_name": "arthur.chini@pwc.com",
            "permission_level": "CAN_MANAGE_RUN"
            }
        ],
        "run_as": {
            "user_name": "gabriel.apimenta@pwc.com"
        },
        "tasks": tasks,
        "max_concurrent_runs": 10
        }

    json_str = json.dumps(job_config, indent=4)
    print(json_str)
    

