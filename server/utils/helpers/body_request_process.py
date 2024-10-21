from utils.constants.funds import FUNDS
from utils.constants.notebooks import NOTEBOOKS
from utils.constants.notebooks_tasks import NOTEBOOKS_TASKS


def create_request_body(fundo_alvo, index):
    
    
    request_body = {
        "name": fundo_alvo,
        "run_name": fundo_alvo,
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
        "tasks": [
            {
            "task_key": "GUARDIAN_MULTAI_CONSIGNADO_III_FUNDO_DE_INVESTIMENTO_EM_DIREITOS_CREDITORIOS",
            "run_job_task": {
                "job_parameters": {
                "fundo": fundo_alvo
                },
                "job_id": "539449877491210"
            },
            "timeout_seconds": 3600
            }
        ]
        }

   
    return request_body

