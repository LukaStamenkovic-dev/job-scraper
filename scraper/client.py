import requests


class HttpClient:

    def get(self, url):
        response = requests.get(url)
        response.raise_for_status()

        return response.json()