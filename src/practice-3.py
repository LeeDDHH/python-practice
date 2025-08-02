import cloudscraper
from abc import abstractmethod  # abcモジュールをインポート
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from typing import TypedDict


base_url = "https://weworkremotely.com"
target_path = "/remote-full-time-jobs"


class JobData(TypedDict):
    title: str
    company: str
    head_quater: str
    categories: str
    url: str


class Scraper:
    def __init__(self, base_url: str, target_path: str):
        self.base_url: str = base_url
        self.target_path: str = target_path
        self.job_list: list[JobData] = []

    def get_content(self, url) -> BeautifulSoup:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @abstractmethod
    def get_jobs_data(self) -> None:
        pass

    @abstractmethod
    def _get_jobs_per_page(self, url: str, last_page_number: int) -> None:
        pass

    @abstractmethod
    def _get_jobs(self) -> None:
        pass

    @abstractmethod
    def _shape_job_data(self, job) -> JobData:
        pass

    @abstractmethod
    def _print_jobs(self) -> None:
        pass

    @abstractmethod
    def _get_job_url(self, url: str) -> str:
        pass

    @abstractmethod
    def _print_job_details(self,
                           title: str,
                           company: str,
                           head_quater: str,
                           categories: str,
                           url: str
                           ) -> None:
        pass


class WeworkRemotelyScraper(Scraper):
    def __init__(self, base_url: str, target_path: str):
        super().__init__(base_url, target_path)

    def get_jobs_data(self) -> None:
        try:
            soup = self.get_content(f"{self.base_url}{self.target_path}")
            pagination = soup.find("div", {"class": "pagination"})
            last = pagination.find("span", {"class": "last"})
            last_url = urlparse(last.find("a")["href"])
            params = parse_qs(last_url.query)
            last_page_number = params['page'][0]
            self._get_jobs_per_page(
                f"{self.base_url}{self.target_path}",
                int(last_page_number)
            )
        except (AttributeError, KeyError, IndexError):
            self._get_jobs(f"{self.base_url}{self.target_path}")
            return self._print_jobs()

    def _get_jobs_per_page(self, url: str, last_page_number: int) -> None:
        for page in range(1, last_page_number + 1):
            self._get_jobs(f"{url}?page={page}")
        self._print_jobs()

    def _get_jobs(self, url: str) -> None:
        soup = self.get_content(url)
        jobs = soup.find("section", {"class": "jobs"}).find_all("li")[0:-1]
        for job in jobs:
            job_data = self._shape_job_data(job)
            self.job_list.append(job_data)

    def _shape_job_data(self, job) -> JobData:
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
            })
        head_quater = head_quater.text if head_quater else "Not registered"
        categories = job.find_all("p", {
            "class": "new-listing__categories__category"
            })
        categories = [category.text for category in categories]
        categories = Util.str_list_to_str(categories)
        url = self._get_job_url(job.find_all("a"))
        return {
            "title": title,
            "company": company,
            "head_quater": head_quater,
            "categories": categories,
            "url": url
        }

    def _print_jobs(self) -> None:
        for job in self.job_list:
            self._print_job_details(**job)

    def _get_job_url(self, url: str) -> str:
        if not url:
            return ""
        elif len(url) >= 2:
            return f"{self.base_url}{url[1]['href']}"
        else:
            return f"{self.base_url}{url[0]['href']}"

    def _print_job_details(self,
                           title: str,
                           company: str,
                           head_quater: str,
                           categories: str,
                           url: str
                           ) -> None:
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Headquarters: {head_quater}")
        print(f"Categories: {categories}")
        print(f"URL: {url}")
        print("-" * 40)


class Util:
    @staticmethod
    def str_list_to_str(str_list) -> str:
        return ", ".join(str_list)


WeworkRemotelyScraper = WeworkRemotelyScraper(base_url, target_path)
WeworkRemotelyScraper.get_jobs_data()
