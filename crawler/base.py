class BaseCrawler:
    def __init__(self, keyword, max_pages=1):
        self.keyword = keyword
        self.max_pages = max_pages

    def fetch(self):
        raise NotImplementedError
