class Job:

    def __init__(
        self,
        job_title,
        company,
        description,
        location_raw,
        address,
        city,
        country,
        salary_raw,
        salary_min,
        salary_max,
        language,
        employment_type,
        experience_level,
        visa_sponsorship,
        job_url,
        source_site,
        external_job_id,
        is_external,
        technologies,
        id=None,
    ):
        self.id = id
        self.job_title = job_title
        self.company = company

        self.description = description

        self.location_raw = location_raw
        self.address = address
        self.city = city
        self.country = country

        self.salary_raw = salary_raw
        self.salary_min = salary_min
        self.salary_max = salary_max

        self.language = language
        self.employment_type = employment_type
        self.experience_level = experience_level
        self.visa_sponsorship = visa_sponsorship

        self.job_url = job_url
        self.source_site = source_site
        self.external_job_id = external_job_id
        self.is_external = is_external

        self.technologies = technologies