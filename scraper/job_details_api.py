from scraper.client import HttpClient


class JobDetailsApi:

    def __init__(self):
        self.client = HttpClient()

    def get_job_details(self, job_url):
        url = f"https://germantechjobs.de/api/jobWithUrl/{job_url}"

        response = self.client.get(url)

        return response