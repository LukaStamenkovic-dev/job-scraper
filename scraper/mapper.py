from models.job import Job


class JobMapper:

    def from_json(self, job_json):
        return Job(
            job_title=job_json["name"],
            company=job_json["company"],
            description=None,
            location_raw=job_json["actualCity"],
            address=job_json["address"],
            city=job_json["actualCity"],
            country="Germany",
            salary_raw=None,
            salary_min=job_json["annualSalaryFrom"],
            salary_max=job_json["annualSalaryTo"],
            language=job_json["language"],
            employment_type=job_json["jobType"],
            experience_level=job_json["expLevel"],
            visa_sponsorship=job_json["hasVisaSponsorship"],
            job_url=job_json["jobUrl"],
            source_site="GermanTechJobs",
            external_job_id=job_json["_id"],
            is_external=False,
            technologies=job_json["technologies"]
        )