from playwright.sync_api import sync_playwright


class PlaywrightManager:
    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)

    def new_page(self):
        return self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()
