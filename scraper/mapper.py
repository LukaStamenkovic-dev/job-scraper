from models.job import Job

class JobMapper:

    def from_json(self, job_json):
        return Job(job_title = job_json["name"],
                   company = job_json["company"],
                    city = job_json["actualCity"],
                    address = job_json["address"],
                    language = job_json["language"],
                    job_url = job_json["jobUrl"],
                    salary_min = job_json["annualSalaryFrom"],
                    salary_max = job_json["annualSalaryTo"],
                    technologies = job_json["technologies"])
