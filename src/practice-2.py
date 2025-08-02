import cloudscraper
from abc import abstractmethod  # abcモジュールをインポート
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com"
target_path = "/categories/remote-full-stack-programming-jobs#job-listings"


class Scraper:
    def __init__(self, base_url, target_path):
        self.base_url = base_url
        self.target_path = target_path
        self.job_list = []

    def get_content(self):
        scraper = cloudscraper.create_scraper()
        response = scraper.get(f"{self.base_url}{self.target_path}")
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @abstractmethod
    def get_jobs(self):
        pass


class WeworkRemotelyScraper(Scraper):
    def __init__(self, base_url, target_path):
        super().__init__(base_url, target_path)

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
            url = self._get_job_url(job.find_all("a"))
            job_data = {
                "title": title,
                "company": company,
                "head_quater": head_quater,
                "categories": categories,
                "url": url
            }
            self.job_list.append(job_data)
        return self.job_list

    def print_jobs(self):
        jobs = self.get_jobs()
        for job in jobs:
            self._print_job_details(**job)

    def _get_job_url(self, url):
        if not url:
            return None
        elif len(url) >= 2:
            return f"{self.base_url}{url[1]['href']}"
        else:
            return f"{self.base_url}{url[0]['href']}"

    def _print_job_details(self, title, company, head_quater, categories, url):
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Headquarters: {head_quater}")
        print(f"Categories: {categories}")
        print(f"URL: {url}")
        print("-" * 40)


class Util:
    @staticmethod
    def str_list_to_str(str_list):
        return ", ".join(str_list)


WeworkRemotelyScraper = WeworkRemotelyScraper(base_url, target_path)
WeworkRemotelyScraper.print_jobs()
