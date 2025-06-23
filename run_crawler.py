from crawler.weibo import WeiboCrawler
from analyzer.sentiment import SentimentAnalyzer
from storage.mongodb import MongoStorage

def main():
    keyword = "新能源"
    max_pages = 2
    crawler = WeiboCrawler(keyword, max_pages)
    posts = crawler.fetch()
    print(f"采集到 {len(posts)} 条微博数据")

    analyzer = SentimentAnalyzer()
    for post in posts:
        post.update(analyzer.analyze(post["text"]))

    db = MongoStorage()
    db.insert_posts(posts)
    print("数据已写入MongoDB，示例：", posts[0] if posts else "无数据")

if __name__ == "__main__":
    main()
