# coding: utf-8
# 版权所有：该文件第一版权人为王振中（298046805）


class UrlManager(object):
    # 需要对应的数据结构来存储待爬取的链接们和已爬取的链接们
    def __init__(self):
        self.new_urls = set() # 待爬取链接
        self.old_urls = set() # 已爬取链接

    # 添加单个网址到待爬取链接堆中
    #
    # _url:代表传入的网址，如果该网址不是已经爬取过的链接或者已经
    #     在待爬取链接堆中，则添加到待爬取链接堆里
    #
    # 无返回值
    def add_url(self, _url):
        # 非空判断
        if _url is None:
            return
        if _url not in self.new_urls and _url not in self.old_urls:
            self.new_urls.add(_url)

    # 添加多个链接
    def add_new_urls(self, new_urls):
        # 非空判断,待添加链接堆为空或者长度为0
        if new_urls is None or len(new_urls) == 0:
            return
        # for i in range(1,11):
        #     pass
        for _url in new_urls:
            self.add_url(_url)

    # 判断是否有链接可以爬取
    def has_url(self):
        return len(self.new_urls)>0

    # 将获得的网址先存进已爬取链接堆，再返回给调度器
    def get_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url
