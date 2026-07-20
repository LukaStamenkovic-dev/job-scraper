from database.repositories.job_repository import JobRepository
from models.company import Company
from services.company_service import CompanyService


class JobService:

    def __init__(self):
        self.job_repository = JobRepository()
        self.company_service = CompanyService()

    def save_job(self, job):
        if self.job_repository.exists_by_job_url(job.job_url):
            return None

        company = Company(
        name=job.company,
        website_url=None,
        company_size=None,
        company_type=None,
    )

        saved_company = self.company_service.get_or_create(company)

        return self.job_repository.create(job, saved_company.id)