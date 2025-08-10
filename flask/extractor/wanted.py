from modules.wanted_scraper import JobScraper


def extract_wanted_jobs(keywords):
    wanted_scraper = JobScraper(keywords)
    wanted_scraper.scrape_jobs()
    return wanted_scraper.jobs_db
