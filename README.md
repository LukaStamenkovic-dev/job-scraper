# GermanTechJobs Job Scraper

> A Python application that collects job advertisements from the GermanTechJobs platform, retrieves detailed job information, and stores the data in a normalized MySQL database using a layered architecture.

The scraper downloads both job listings and detailed job information, processes the collected data, and stores companies, jobs, and technologies while preventing duplicate records.

---

## Features

- Scrapes all available jobs from the GermanTechJobs API
- Retrieves detailed information for every job
- Stores companies only once
- Stores technologies only once
- Creates many-to-many relationships between jobs and technologies
- Prevents duplicate job entries
- Uses a layered architecture
- Uses MySQL for data persistence

---

## Project Structure

```
job-scraper/
│
├── database/
│   ├── connection.py
│   └── repositories/
│
├── models/
│
├── scraper/
│   ├── client.py
│   ├── jobs_api.py
│   ├── job_details_api.py
│   ├── job_mapper.py
│   └── job_details_mapper.py
│
├── services/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Architecture

The application follows a layered architecture where each layer has a single responsibility.

```
GermanTechJobs API
        │
        ▼
JobsApi / JobDetailsApi
        │
        ▼
Mappers
        │
        ▼
Models
        │
        ▼
Services
        │
        ▼
Repositories
        │
        ▼
MySQL Database
```

### Layer Responsibilities

| Layer | Responsibility |
|--------|----------------|
| API | Downloads data from GermanTechJobs |
| Mappers | Converts JSON responses into Python objects |
| Models | Represents application entities |
| Services | Contains business logic |
| Repositories | Handles database operations |

---

## Execution Flow

The scraper performs the following steps:

1. Downloads all available jobs from the GermanTechJobs API.
2. Maps each JSON object into a `Job` model.
3. Requests detailed information for every job.
4. Updates the existing `Job` object with additional details.
5. Checks whether the company already exists.
6. Creates the company if necessary.
7. Checks whether technologies already exist.
8. Creates missing technologies.
9. Saves the job.
10. Creates many-to-many relationships between jobs and technologies.
11. Repeats the process until all jobs have been processed.

---

## Database

The project uses a normalized MySQL database.

### Companies

Stores unique companies.

Example fields:

- id
- name
- website_url
- company_size
- company_type

---

### Jobs

Stores job advertisements.

Example fields:

- company_id
- job_title
- description
- address
- city
- country
- salary_min
- salary_max
- salary_currency
- salary_period
- experience_level
- employment_type
- language
- visa_sponsorship
- job_url
- external_job_id
- source_site
- scraped_at
- updated_at

---

### Technologies

Stores unique technologies.

Examples:

- Python
- Java
- Docker
- Kubernetes

---

### Job Technologies

Stores the many-to-many relationship between jobs and technologies.

---

## Technologies Used

- Python 3
- MySQL
- Requests
- mysql-connector-python
- python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LukaStamenkovic-dev/job-scraper.git
```

Navigate to the project:

```bash
cd job-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

Run the application:

```bash
python main.py
```

---

## Example Output

```
Processing 1/1449
Processing 2/1449
...
Processing 1449/1449

Imported 1449 jobs
Finished in 437.73 seconds
```

---

## Design Principles

The project follows several software engineering principles:

- Separation of Concerns
- Single Responsibility Principle (SRP)
- Repository Pattern
- Service Layer Pattern
- Object Mapping
- Database Normalization

These principles make the project easier to maintain, test, and extend.

---

## Future Improvements

Possible future enhancements include:

- Parallel HTTP requests for faster execution
- Retry mechanism for failed API requests
- Structured logging
- Command-line configuration
- Support for additional job platforms

---

## Author

**Luka Stamenkovic**

GitHub: https://github.com/LukaStamenkovic-dev
