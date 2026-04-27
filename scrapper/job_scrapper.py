from selenium.webdriver.common.by import By
import time

def scrape_jobs(driver):
    jobs = []

    for page in range(1, 4):  # 3 pages
        url = f"https://remoteok.com/remote-dev-jobs?page={page}"
        driver.get(url)

        time.sleep(5)

        job_cards = driver.find_elements(By.CSS_SELECTOR, "tr.job")
        print(f"Page {page}: Found {len(job_cards)} jobs")

        for job in job_cards:
            try:
                title = job.find_element(By.TAG_NAME, "h2").text
                company = job.find_element(By.TAG_NAME, "h3").text

                jobs.append({
                    "Title": title,
                    "Company": company
                })
            except:
                continue

    return jobs