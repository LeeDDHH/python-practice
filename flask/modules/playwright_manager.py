from playwright.sync_api import sync_playwright

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"


class PlaywrightManager:
    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)

    def new_page(self):
        return self.browser.new_page(user_agent=user_agent)

    def close(self):
        self.browser.close()
        self.playwright.stop()
