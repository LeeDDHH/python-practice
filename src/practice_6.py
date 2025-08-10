from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

base_url = "https://www.wanted.co.kr/"
keywords = ['flutter', 'nextjs', 'kotlin']
csv_first_row = ["title", "url", "company_name", "reward"]


class Job:
    def __init__(self, job):
        self.title = self._get_title(job)
        self.url = self._get_url(job)
        self.company_name = self._get_company_name(job)
        self.reward = self._get_reward(job)

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "company_name": self.company_name,
            "reward": self.reward
        }

    def _get_title(self, job):
        strong_tag = job.find("strong")
        return strong_tag.text if strong_tag else "No title"

    def _get_url(self, job):
        url_tag = job.find('a')
        return f"{base_url}{url_tag['href']}" if url_tag else "No URL"

    def _get_company_name(self, job):
        company_name_tag = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6")
        return company_name_tag.text if company_name_tag else "No Company Name"

    def _get_reward(self, job):
        reward_tag = job.find('span', class_='JobCard_reward__oCSIQ')
        return reward_tag.text if reward_tag else "No Reward"


class PlaywrightManager:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)

    def new_page(self):
        return self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()


class JobScraper:
    def __init__(self, keyword):
        self.content = self._get_content(keyword)
        self.jobs_db = []

    def _get_content(self, keyword):
        p = PlaywrightManager()
        page = p.new_page()
        page.goto(f"{base_url}/search?query={keyword}&tab=position")

        for i in range(5):
            time.sleep(5)
            page.keyboard.down("End")

        content = page.content()
        p.close()

        return content

    def scrape_jobs(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", role="listitem")

        for job in jobs:
            self.jobs_db.append(Job(job).to_dict())


class CSVWriter:
    def __init__(self, filename):
        self.filePath = f"./src/files/{filename}_jobs.csv"

    def write(self, datas):
        file = open(self.filePath, mode='w', newline='')

        writer = csv.writer(file)
        writer.writerow(csv_first_row)
        for data in datas:
            writer.writerow(data.values())

        file.close()


for keyword in keywords:
    scraper = JobScraper(keyword)
    scraper.scrape_jobs()
    csv_writer = CSVWriter(keyword)
    csv_writer.write(scraper.jobs_db)
