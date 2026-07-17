from scraper.api import JobsApi


def main():
    api = JobsApi()

    jobs = api.get_jobs()

    print(f"Number of jobs: {len(jobs)}")
    print(jobs[0].job_title)
    print(jobs[0].company)
    print(jobs[0].salary_min)
    print(jobs[0].technologies)


if __name__ == "__main__":
    main()