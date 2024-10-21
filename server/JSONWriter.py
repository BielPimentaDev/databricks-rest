import json
import os

class JsonFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        """Escreve dados em um arquivo JSON."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read(self):
        """Lê dados de um arquivo JSON e retorna um dicionário."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"O arquivo '{self.filename}' não foi encontrado.")
        
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        

        

# Exemplo de uso:
