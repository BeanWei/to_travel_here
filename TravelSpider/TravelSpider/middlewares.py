# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random  
import requests
import os


class TravelspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TravelspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

#  自定义代理中间件(此处使用蘑菇代理，可以自己修改和匹配)
class ProxyMiddleware(object):
    s = requests.session()
    s.keep_alive = False

    def __init__(self):
        self.url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=91a4450c3b98477bcfead8c060db8d&count=10&expiryDate=5&format=2"
        self.proxy = requests.get(self.url).text.split("\r\n")[0:-1]
        self.counts = 0

    def process_request(self, request, spider):
        #  这里作一个计数器,在访问次数超过1000次之后就切换一批(10个)高匿代理,使得代理一直保持最新的状态
        if self.counts < 1000:
            pre_proxy = random.choice(self.proxy)
            request.meta['proxy'] = 'https://{}'.format(pre_proxy)
            self.counts += 1
        else:
            # 进入到这里的这一次就不设定代理了,直接使用本机ip访问
            self.counts = 0
            self.proxy = requests.get(self.url).text.split("\r\n")[0:-1]

class myProxyMiddleware(object):
    def __init__(self):
        self.file = open(os.path.abspath(os.path.dirname(__file__))+'/ProxyPools.txt')

    def process_request(self, request, spider):
        ip = random.choice(self.file.readlines())
        request.meta['proxy'] = "http://"+str(ip)




