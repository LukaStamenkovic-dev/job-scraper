# from scraper.jobs_api import JobsApi
# from scraper.job_details_api import JobDetailsApi
# from services.job_service import JobService
# import json


# def main():
#     jobs_api = JobsApi()
#     job_service = JobService()
#     job_details_api = JobDetailsApi()

#     jobs = jobs_api.get_jobs()

#     details = job_details_api.get_job_details(jobs[0].job_url)

#     print(json.dumps(details, indent=4))

#     for job in jobs:
#         job_service.save_job(job)

#     print(f"Imported {len(jobs)} jobs")


# if __name__ == "__main__":
#     main()

import time

from scraper.jobs_api import JobsApi
from services.job_service import JobService


def main():
    start = time.time()

    jobs_api = JobsApi()
    job_service = JobService()

    jobs = jobs_api.get_jobs()

    for job in jobs:
        job_service.save_job(job)

    end = time.time()

    print(f"\nImported {len(jobs)} jobs")
    print(f"Finished in {end - start:.2f} seconds")


if __name__ == "__main__":
    main()