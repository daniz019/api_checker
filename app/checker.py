import requests

class ApiChecker:
    def __init__(self, url, timeout=5):
        self.url = url
        self.timeout = timeout

    def check_status(self):
        try:
            response = requests.get(self.url, timeout=self.timeout)
            return response.status_code
        except Exception as e:
            return str(e)