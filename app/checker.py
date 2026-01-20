import requests
from requests.exceptions import ConnectionError, Timeout, RequestException


class ApiChecker:
    def __init__(self, url, timeout=5):
        self.url = url
        self.timeout = timeout

    def check_status(self):
        try:
            response = requests.get(self.url, timeout=self.timeout)
            return response.status_code
        except ConnectionError:
            return "Erro de Conexão (DNS ou rede indisponível)"
        except Timeout:
            return "Timeout: A requisição demorou demais"
        except RequestException as e:
            return f"Erro de Requisição: {e}"