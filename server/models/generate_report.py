from flask import jsonify
import requests
from ExternalAPI import DatabricksRest
from JSONWriter import JsonFileHandler

databricksRest = DatabricksRest()

def history_run():
    query_params = {
        'job_id': '838799931042262',
    }
    
    try:
        data = databricksRest.get('jobs/runs/list', params=query_params) 
        return(data)
    except requests.HTTPError as e:
        return jsonify(error=str(e)), e.response.status_code

def get_job_run(run_id):
    query_params = {
        'run_id': run_id,
    }
    try:
        data = databricksRest.get('jobs/runs/get', params=query_params) 
        return(data)
    except requests.HTTPError as e:
        return jsonify(error=str(e)), e.response.status_code

def get_job_output(run_id):
    query_params = {
        'run_id': run_id,
    }
    
    try:
        data = databricksRest.get('jobs/runs/get-output', params=query_params) 
        return((data))
    except requests.HTTPError as e:
        return jsonify(error=str(e)), e.response.status_code

def generate_report():
    history = history_run()
    relatorio = []
    latest_run = history["runs"][0]
    batimento_julho = get_job_run(latest_run["run_id"])
    mes = batimento_julho["job_parameters"][0]["default"]
    tasks = batimento_julho["tasks"]
    handler = JsonFileHandler("relatorios.json")
    fundos_analisados = []
    for task in tasks:
        fundo = get_job_output(task["run_id"])
        fundo_metadata = fundo["metadata"]
        nome_fundo = fundo_metadata["tasks"][0]["run_job_task"]["job_parameters"]["fundo"]
        if fundo_metadata["state"]["result_state"] == "FAILED":
            fundo_id = fundo["run_job_output"]["run_id"]
            fundo_job_run = get_job_run(fundo_id)
            batimentos = fundo_job_run["tasks"]
            lista_batimentos = []
            for batimento in batimentos:
                if batimento["state"]["result_state"] == "FAILED":                              
                    output_batimento = get_job_output(batimento["run_id"])                
                    batimento_analise = {"batimento" : batimento["task_key"], "erro" : output_batimento["error"], "link": output_batimento["metadata"]["run_page_url"]}
                    lista_batimentos.append(batimento_analise)
            print("batimentos")
            print(lista_batimentos)
            fundos_analisados.append({"fundo": nome_fundo, "batimentos" : lista_batimentos })
        print("fundo")
        print(fundos_analisados)
            
    relatorio.append({"mes" : mes, "fundos" : fundos_analisados })
    handler.write(relatorio)