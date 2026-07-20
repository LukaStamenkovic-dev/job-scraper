from scraper.jobs_api import JobsApi
from services.job_service import JobService


def main():
    jobs_api = JobsApi()
    job_service = JobService()

    jobs = jobs_api.get_jobs()

    for job in jobs:
        job_service.save_job(job)

    print(f"Imported {len(jobs)} jobs")


if __name__ == "__main__":
    main()