import cloudscraper
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

cloudscraper = cloudscraper.create_scraper()
response = cloudscraper.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", {"class": "jobs"}).find_all("li")[0:-1]

for job in jobs:
    title = job.find("h4", {"class": "new-listing__header__title"}).text
    company = job.find("p", {"class": "new-listing__company-name"}).text
    head_quater = job.find("p", {"class": "new-listing__company-headquarters"}).text
    categories = job.find_all("p", {
        "class": "new-listing__categories__category"
        })
    categories = [category.text for category in categories]
    categories = ", ".join(categories)
    print(title, "----", company, "----", head_quater, "----", categories)
