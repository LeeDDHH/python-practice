from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

base_url = "https://www.wanted.co.kr/"

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(3)

page.click('button[aria-controls="nav_searchbar"]')

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요").fill("flutter")

time.sleep(3)

page.keyboard.press("Enter")

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5)

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

time.sleep(5)

content = page.content()

browser.close()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", role="listitem")

jobs_db = []

for job in jobs:
    url = f"{base_url}{job.find('a')['href']}"
    title = job.find("strong").text
    company_name = job.find(
        "span",
        class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6",
    ).text
    reward = job.find('span', class_='JobCard_reward__oCSIQ').text
    job = {
        "title": title,
        "url": url,
        "company_name": company_name,
        "reward": reward
    }

    jobs_db.append(job)

print(len(jobs_db))
print(jobs_db)
