import cloudscraper
from abc import abstractmethod  # abcモジュールをインポート
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"


class Scraper:
    def __init__(self, url):
        self.url = url
        self.job_list = []

    def get_content(self):
        scraper = cloudscraper.create_scraper()
        response = scraper.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @abstractmethod
    def get_jobs(self):
        pass


class WeworkRemotelyScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def get_jobs(self):
        soup = self.get_content()
        jobs = soup.find("section", {"class": "jobs"}).find_all("li")[0:-1]
        for job in jobs:
            title = job.find(
                "h4",
                {
                    "class": "new-listing__header__title"
                }).text
            company = job.find(
                "p",
                {
                    "class": "new-listing__company-name"
                }).text
            head_quater = job.find("p", {
                "class": "new-listing__company-headquarters"
                }).text
            categories = job.find_all("p", {
                "class": "new-listing__categories__category"
                })
            categories = [category.text for category in categories]
            categories = Util.str_list_to_str(categories)
            job_data = {
                "title": title,
                "company": company,
                "head_quater": head_quater,
                "categories": categories
            }
            self.job_list.append(job_data)
        return self.job_list

    def print_jobs(self):
        jobs = self.get_jobs()
        for job in jobs:
            Util.print_job_details(**job)


class Util:
    @staticmethod
    def print_job_details(title, company, head_quater, categories):
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Headquarters: {head_quater}")
        print(f"Categories: {categories}")
        print("-" * 40)

    @staticmethod
    def str_list_to_str(str_list):
        return ", ".join(str_list)


WeworkRemotelyScraper = WeworkRemotelyScraper(url)
WeworkRemotelyScraper.print_jobs()
