from .base import BaseCrawler
from playwright.sync_api import sync_playwright
import time
import json
import os

class WeiboCrawler(BaseCrawler):
    def fetch(self):
        results = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            # 载入 cookie
            if os.path.exists("weibo_cookies.json"):
                with open("weibo_cookies.json", "r", encoding="utf-8") as f:
                    cookies = json.load(f)
                context.add_cookies(cookies)
            page = context.new_page()
            for page_num in range(1, self.max_pages + 1):
                url = f"https://s.weibo.com/weibo?q={self.keyword}&page={page_num}"
                page.goto(url, timeout=60000)
                page.wait_for_timeout(4000)
                cards = page.query_selector_all("div.card")  # 注意此class需与你页面一致
                for card in cards:
                    text_tag = card.query_selector("p.txt")
                    user_tag = card.query_selector(".name")
                    time_tag = card.query_selector(".from")
                    if text_tag:
                        text = text_tag.inner_text().strip()
                        user = user_tag.inner_text().strip() if user_tag else ""
                        timestamp = time_tag.inner_text().strip() if time_tag else time.strftime("%Y-%m-%d %H:%M:%S")
                        results.append({
                            "platform": "weibo",
                            "user": user,
                            "text": text,
                            "timestamp": timestamp
                        })
                time.sleep(1)
            browser.close()
        return results

if __name__ == "__main__":
    # 单测采集是否有数据
    crawler = WeiboCrawler("新能源", 1)
    print(crawler.fetch())
