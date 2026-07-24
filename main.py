import time

from scraper.jobs_api import JobsApi
from services.job_service import JobService


def main():
    start = time.time()

    jobs_api = JobsApi()
    job_service = JobService()

    jobs = jobs_api.get_jobs()

    for index, job in enumerate(jobs, start=1):
        print(f"Saving {index}/{len(jobs)}")
        job_service.save_job(job)

    end = time.time()

    print(f"\nImported {len(jobs)} jobs")
    print(f"Finished in {end - start:.2f} seconds")


if __name__ == "__main__":
    main()