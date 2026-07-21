from models.job import Job

class JobDetailsMapper:

    def update_job(self, job: Job, details_json):
        job.description = details_json.get("description")
        job.employment_type = details_json.get("jobType")
        job.experience_level = details_json.get("expLevel")
        job.visa_sponsorship = details_json.get("hasVisaSponsorship")