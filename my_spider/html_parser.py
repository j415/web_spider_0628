# coding: utf-8
# 版权所有：该文件第一版权人为王振中（298046805）
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup as beauty

class HtmlParser(object):
    # 需要在类中存储要解析出的新跳转链接们和有价值的数据
    def __init__(self):
        self.new_urls = [] # 数组，集合
        self.new_datas = [] # 字典，KEY-VALUE

    def parse(self, current_html, current_url):
        # 非空判断
        if current_html is None or current_url is None:
            return

        # "html.parser"为BS4所使用的具体解析器名称，可指定不同的解析器
        soup = beauty(current_html,"html.parser")

        self.new_urls = self._get_new_urls(soup, current_url)
        self.new_datas = self._get_new_datas(soup, current_url)

        return self.new_datas,self.new_urls

    # 获得有价值的数据
    def _get_new_datas(self, soup, current_url):
        _new_data = {}
        _new_data["url"] = current_url # 记录数据网址

        # 数据对应的网页标题
        title = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        _new_data["title"] = title

        # 对应网页的文字内容
        summary = soup.find("div",class_="lemma-summary")
        _new_data["summary"] = summary.get_text()

        return _new_data

    # 获得新的完整跳转链接
    def _get_new_urls(self, soup, current_url):
        _new_urls = set()

        # 可以通过正则表达式来匹配findall查询的内容
        # python中正则表达式的库为re
        # ".*?"作为万能匹配，要学会使用
        # links = soup.findAll('a', href=re.compile("/item/\d+\.htm"))
        links = soup.findAll('a', href=re.compile(""))

        for link in links:
            new_url = link["href"]
            # 使用urllib.parse的urljoin方法来进行完整网址的拼接
            true_url = urljoin(current_url, new_url)
            _new_urls.add(true_url)

        return _new_urls