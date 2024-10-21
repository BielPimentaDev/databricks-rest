import requests

token = 'dapi0623242a7e6f05190933214f08f250f5-3'
url = 'https://adb-3694987222772985.5.azuredatabricks.net/api/2.1/jobs/create'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}  

class DatabricksRest:
    def __init__(self):
        self.base_url = 'https://adb-3694987222772985.5.azuredatabricks.net/api/2.1/'
        self.token = 'dapi0623242a7e6f05190933214f08f250f5-3'
        
    def _get_headers(self):
        """Gera os cabeçalhos para a requisição, incluindo o Bearer Token."""
        headers = {}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers
    
    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()
