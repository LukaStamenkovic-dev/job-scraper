from scraper.api import JobsApi


def main():
    api = JobsApi()

    jobs = api.get_jobs()

    print(f"Number of jobs: {len(jobs)}")
    print(jobs[0])


if __name__ == "__main__":
    main()



# from scraper.client import HttpClient


# def main():
#     client = HttpClient()

#     search_url = input("Enter search URL: ").strip()

#     html = client.get(search_url)

#     with open("search_page.html", "w", encoding="utf-8") as file:
#         file.write(html)

#     print("HTML successfully saved to search_page.html")


# if __name__ == "__main__":
#     main()

