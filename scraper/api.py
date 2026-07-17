from scraper.client import HttpClient


class JobsApi:

    BASE_URL = "https://germantechjobs.de/api"

    def __init__(self):
        self.client = HttpClient()

    def get_jobs(self):
        return self.client.get(f"{self.BASE_URL}/jobsLight")