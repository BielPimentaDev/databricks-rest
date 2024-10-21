from flask import jsonify

from JSONWriter import JsonFileHandler



class JobRunsModel:
    def __init__(self):
        self.handler = JsonFileHandler("relatorios.json")
        
    def select_error(self, error):
        try:
            dados_lidos = self.handler.read()
            filtered_data = [
                {
                    'mes': entry['mes'],
                    'fundos': [
                        {
                            'fundo': fundo['fundo'],
                            'batimentos': [
                                batimento for batimento in fundo['batimentos']
                                if batimento['erro'].startswith(error)
                            ]
                        }
                        for fundo in entry['fundos']
                        if any(batimento['erro'].startswith('IndexError') for batimento in fundo['batimentos'])
                     ],
                    'total_batimentos': sum(
                        len([batimento for batimento in fundo['batimentos'] if batimento['erro'].startswith('IndexError')])
                        for fundo in entry['fundos']
                    )
                    
                }
                for entry in dados_lidos
            ]

            return(filtered_data)
        except FileNotFoundError as e:
            print(e)
            
