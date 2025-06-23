from .base import BaseCrawler
from datetime import datetime

class DouyinCrawler(BaseCrawler):
    def fetch(self):
        return [
            {
                "platform": "douyin",
                "user": f"抖音用户{i}",
                "text": f"这是关于 {self.keyword} 的抖音内容示例{i}",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for i in range(1, self.max_pages + 1)
        ]
