from database.repositories.job_repository import JobRepository
from database.repositories.job_technology_repository import JobTechnologyRepository
from models.company import Company
from models.technology import Technology
from services.company_service import CompanyService
from services.technology_service import TechnologyService


class JobService:

    def __init__(self):
        self.job_repository = JobRepository()
        self.job_technology_repository = JobTechnologyRepository()
        self.company_service = CompanyService()
        self.technology_service = TechnologyService()

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
        saved_job = self.job_repository.create(job, saved_company.id)

        for technology_name in job.technologies:
            technology = Technology(
                        id=None,
                        name=technology_name
                        )
        
            saved_technology = self.technology_service.get_or_create(technology)

            self.job_technology_repository.create(saved_job.id, saved_technology.id)

        return saved_job

