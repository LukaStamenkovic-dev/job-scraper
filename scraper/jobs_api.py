from scraper.client import HttpClient
from scraper.job_mapper import JobMapper
from scraper.job_details_api import JobDetailsApi
from scraper.job_details_mapper import JobDetailsMapper


class JobsApi:

    BASE_URL = "https://germantechjobs.de/api"

    def __init__(self):
        self.client = HttpClient()
        self.mapper = JobMapper()
        self.job_details_api = JobDetailsApi()
        self.job_details_mapper = JobDetailsMapper()

    def get_jobs(self):
        jobs_json = self.client.get(f"{self.BASE_URL}/jobsLight")

        jobs = []

        total_jobs = len(jobs_json)

        for index, job_json in enumerate(jobs_json, start=1):
            print(f"Processing {index}/{total_jobs}")

            job = self.mapper.from_json(job_json)

            details_json = self.job_details_api.get_job_details(job.job_url)

            self.job_details_mapper.update_job(job, details_json)

            jobs.append(job)

        return jobs