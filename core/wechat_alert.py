import requests

class WeChatAlerter:
    def __init__(self, sendkey: str):
        self.sendkey = sendkey

    def send(self, title: str, content: str):
        url = f"https://sctapi.ftqq.com/{self.sendkey}.send"
        data = {
            "title": title,
            "desp": content
        }
        resp = requests.post(url, data=data)
        return resp.json()
