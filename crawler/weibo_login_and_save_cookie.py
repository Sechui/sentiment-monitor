from playwright.sync_api import sync_playwright
import json
import time

def save_cookies_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://weibo.com/login.php")
        print("请在弹出的浏览器窗口内手动登录微博，完成后按回车继续...")
        input()
        cookies = page.context.cookies()
        with open("weibo_cookies.json", "w", encoding="utf-8") as f:
            json.dump(cookies, f)
        print("Cookie已保存到 weibo_cookies.json")
        browser.close()

if __name__ == "__main__":
    save_cookies_after_login()
