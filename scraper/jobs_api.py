from scraper.client import HttpClient
from scraper.mapper import JobMapper


class JobsApi:

    BASE_URL = "https://germantechjobs.de/api"

    def __init__(self):
        self.client = HttpClient()
        self.mapper = JobMapper()

    def get_jobs(self):
        jobs_json = self.client.get(f"{self.BASE_URL}/jobsLight")

        print(jobs_json[0])   # Privremeno

        jobs = []

        for job_json in jobs_json:
            jobs.append(self.mapper.from_json(job_json))

        return jobs
    

