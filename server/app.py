import requests
from JSONWriter import JsonFileHandler
from models.job_runs_model import JobRunsModel
from utils.constants.funds import FUNDS
from utils.constants.notebooks_tasks import NOTEBOOKS_TASKS
from utils.helpers import body_request_process
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

jobRunsModel = JobRunsModel()
handler = JsonFileHandler("relatorios.json")
@app.route('/api', methods=['GET'])
def get_jobs():
    error_parameter = request.args.get('error_parameter')
    try:
        dados_lidos = handler.read()
        if error_parameter:
            return jobRunsModel.select_error(error_parameter)
        return(dados_lidos)
    except FileNotFoundError as e:
        print(e)
        return jsonify(message=e)
    
if __name__ == "__main__":
    app.run()








