import cloudscraper
from abc import abstractmethod  # abcモジュールをインポート
from bs4 import BeautifulSoup


base_url = "https://remoteok.com/"
target_keywords = ["react", "python", "flutter"]


class JobData:
    def __init__(
        self, title: str, company: str, region: str, salary: str, url: str
    ):
        self.title = title
        self.company = company
        self.region = region
        self.salary = salary
        self.url = url


class Scraper:
    def __init__(self, base_url: str, target_keywords: list[str]):
        self.base_url: str = base_url
        self.target_keywords: str = target_keywords
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
    def _shape_regions(self, regions: list[str]) -> str:
        pass

    @abstractmethod
    def _print_jobs(self) -> None:
        pass

    @abstractmethod
    def _get_job_url(self, url: str) -> str:
        pass


class RemoteokScraper(Scraper):
    def __init__(self, base_url: str, target_keywords: list[str]):
        super().__init__(base_url, target_keywords)

    def get_jobs_data(self) -> None:
        for keyword in self.target_keywords:
            url = f"{self.base_url}remote-{keyword}-jobs"
            self._get_jobs(url)
        self._print_jobs()

    # 페이지의 각 직업정보을 가져오기
    def _get_jobs(self, url: str) -> None:
        soup = self.get_content(url)
        jobs = soup.find("table", {"id": "jobsboard"}).find_all(
            "tr", {"class": "job"}
        )
        for job in jobs:
            job_data = self._shape_job_data(job)
            self.job_list.append(job_data)

    # 각 직업정보의 데이터를 정리해서 반환
    def _shape_job_data(self, job) -> JobData:
        title = job.select("h2")[0].text.strip()

        region_and_salary = job.select(".company .location")

        salary = (
            region_and_salary[-1].text.strip()
            if len(region_and_salary) > 1
            else "Not specified"
        )
        region = self._shape_regions(region_and_salary[0:-1])

        company = job.select("h3")[0].text.strip()

        url = job.select(".company a")[0]["href"]

        url = self._get_job_url(job.find_all("a"))
        job_data = JobData(
            title=title, company=company, region=region, salary=salary, url=url
        )
        return job_data

    def _shape_regions(self, regions: list[str]) -> str:
        if not regions:
            return "Not specified"
        shaped_regions = []
        for region in regions:
            region_texts = region.text.split(maxsplit=1)
            if len(region_texts) > 1:
                shaped_regions.append(region_texts[-1])
                continue
            shaped_regions.append(region_texts[0])
        return ", ".join(shaped_regions)

    # 직업정보를 출력
    def _print_jobs(self) -> None:
        for job in self.job_list:
            self._print_job_details(
                title=job.title,
                company=job.company,
                region=job.region,
                salary=job.salary,
                url=job.url,
            )

    # 직업정보 안의 URL을 반환
    def _get_job_url(self, url: str) -> str:
        if not url:
            return ""
        elif len(url) >= 2:
            return f"{self.base_url}{url[1]['href']}"
        else:
            return f"{self.base_url}{url[0]['href']}"

    def _print_job_details(self, **kwargs) -> None:
        for key, value in kwargs.items():
            print(f"{key.capitalize()}: {value}")
        print("-" * 40)


class Util:
    @staticmethod
    # 문자열 리스트를 하나의 문자열로 변환
    def str_list_to_str(str_list) -> str:
        return ", ".join(str_list)


RemoteokScraper = RemoteokScraper(base_url, target_keywords)
RemoteokScraper.get_jobs_data()
