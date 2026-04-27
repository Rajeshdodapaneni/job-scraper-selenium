from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def scrape_jobs(driver):
    driver.get("https://realpython.github.io/fake-jobs/")

    import time
    time.sleep(5)

    jobs = []

    job_cards = driver.find_elements("class name", "card-content")

    print("Found jobs:", len(job_cards))

    for job in job_cards:
        title = job.find_element("class name", "title").text
        company = job.find_element("class name", "company").text

        if "python" in title.lower():
            jobs.append({
            "Title": title,
            "Company": company
            })

    return jobs


import os
def save_to_csv(jobs):
    df = pd.DataFrame(jobs)
    file_path = os.path.abspath("jobs.csv")
    df.to_csv(file_path, index=False)
    print(f"✅ Data saved at: {file_path}")
    print(jobs)


def main():
    driver = get_driver()

    try:
        jobs = scrape_jobs(driver)
        print(f"Scraped {len(jobs)} jobs")
        save_to_csv(jobs)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()


# from scraper.driver_setup import get_driver
# from scraper.job_scraper import scrape_jobs
# from utils.csv_handler import save_to_csv

# def main():
#     driver = get_driver()

#     try:
#         jobs = scrape_jobs(driver)
#         print(f"Total jobs scraped: {len(jobs)}")

#         save_to_csv(jobs)

#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()