from scrapy.core.scheduler import Scheduler

class DupeFilter(object):

    def __init__(self):
        self.jihe=set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):

        if request.url in self.jihe:
            return True

        self.jihe.add(request.url)
        return False

    def open(self):  # can return deferred
        pass

    def close(self, reason):  # can return a deferred
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass
