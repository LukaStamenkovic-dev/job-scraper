from models.job import Job


class JobMapper:

    def from_json(self, job_json):
        return Job(
            job_title=job_json.get("name"),
            company=job_json.get("company"),

            description=None,

            location_raw=job_json.get("actualCity"),
            address=job_json.get("address"),
            city=job_json.get("actualCity"),
            country="Germany",

            salary_raw=None,
            salary_min=job_json.get("annualSalaryFrom"),
            salary_max=job_json.get("annualSalaryTo"),
            salary_currency="EUR",
            salary_period="YEAR",

            language=job_json.get("language"),
            employment_type=job_json.get("jobType"),
            experience_level=job_json.get("expLevel"),
            visa_sponsorship=job_json.get("hasVisaSponsorship"),

            job_url=job_json.get("jobUrl"),
            source_site="GermanTechJobs",
            external_job_id=job_json.get("_id"),
            is_external=bool(job_json.get("redirectJobUrl")),

            technologies=job_json.get("technologies", []),
        )


# STARI JOBMAPPER, treba mi objasnjenje zasto je novi bolji

# from models.job import Job


# class JobMapper:

#     def from_json(self, job_json):
#         return Job(
#             job_title=job_json["name"],
#             company=job_json["company"],
#             description=None,
#             location_raw=job_json["actualCity"],
#             address=job_json["address"],
#             city=job_json["actualCity"],
#             country="Germany",
#             salary_raw=None,
#             salary_min=job_json["annualSalaryFrom"],
#             salary_max=job_json["annualSalaryTo"],
#             language=job_json["language"],
#             employment_type=job_json["jobType"],
#             experience_level=job_json["expLevel"],
#             visa_sponsorship=job_json["hasVisaSponsorship"],
#             job_url=job_json["jobUrl"],
#             source_site="GermanTechJobs",
#             external_job_id=job_json["_id"],
#             is_external=False,
#             technologies=job_json["technologies"]
#         )