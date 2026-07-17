CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    website_url VARCHAR(500),
    logo_url VARCHAR(500),
    company_size VARCHAR(100),
    company_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,

    job_title VARCHAR(255) NOT NULL,
    description TEXT,
    requirements_text TEXT,

    location_raw VARCHAR(500),
    address VARCHAR(255),
    city VARCHAR(150),
    country VARCHAR(100),

    salary_raw VARCHAR(255),
    salary_min DECIMAL(12, 2),
    salary_max DECIMAL(12, 2),
    salary_currency CHAR(3) DEFAULT 'EUR',
    salary_period VARCHAR(50),

    experience_level VARCHAR(100),
    employment_type VARCHAR(100),
    language VARCHAR(100),
    visa_sponsorship BOOLEAN,

    job_url VARCHAR(1000) NOT NULL,
    source_site VARCHAR(100) NOT NULL,
    external_job_id VARCHAR(255),
    is_external BOOLEAN NOT NULL DEFAULT FALSE,

    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_jobs_company
        FOREIGN KEY (company_id)
        REFERENCES companies(id),

    CONSTRAINT uq_jobs_job_url
        UNIQUE (job_url),

    CONSTRAINT uq_jobs_source_external_id
        UNIQUE (source_site, external_job_id)
);

CREATE TABLE technologies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE job_technologies (
    job_id INT NOT NULL,
    technology_id INT NOT NULL,

    PRIMARY KEY (job_id, technology_id),

    CONSTRAINT fk_job_technologies_job
        FOREIGN KEY (job_id)
        REFERENCES jobs(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_job_technologies_technology
        FOREIGN KEY (technology_id)
        REFERENCES technologies(id)
        ON DELETE CASCADE
);