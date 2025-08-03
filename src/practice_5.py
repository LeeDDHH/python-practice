from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(7)

page.click('button[aria-controls="nav_searchbar"]')

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요").fill("flutter")

time.sleep(3)

page.keyboard.press("Enter")

time.sleep(10)

page.click("a#search_tab_position")

time.sleep(7)

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

time.sleep(5)

content = page.content()

browser.close()

p.stop()

soup = BeautifulSoup(content, "html.parser")
