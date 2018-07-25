# coding: utf-8
# 版权所有：该文件第一版权人为王振中（298046805）
from my_spider import url_manager
from my_spider import url_downloader
from my_spider import html_parser
from my_spider import output


class Spider_Main(object):
    # __init__()是Python语法中的构造方法，他在创建对象的同时被自动调用
    def __init__(self):
        # self是本类默认存在的一个对象，可以在类中的任意位置调用类的属性
        self.url_manager = url_manager.UrlManager()# 网址管理器
        self.downloader = url_downloader.UrlDownloader()# 网页下载器
        self.html_parser = html_parser.HtmlParser()# 网页解析器
        self.outputer = output.HtmlOutput()# 输出模块

    # self是python语言默认类中存在本类的一个对象
    def craw(self, first_url):
        # 添加入口网址到网址管理器
        self.url_manager.add_url(first_url)
        craw_times = 0 # 爬取次数
        # 爬虫主逻辑循环，有待爬取地址则不断爬取
        while self.url_manager.has_url():
            try:
                # 获取一个网址进行爬取
                current_url = self.url_manager.get_url()
                # 通过网页下载器下载该网址对应的链接
                current_html = self.downloader.download(current_url)
                # 使用解析器获得有价值的数据和新的待爬取链接们
                new_datas,new_urls = self.html_parser.parse(current_html,current_url)
                # 添加新的待爬取链接们到网址管理器
                self.url_manager.add_new_urls(new_urls)
                # 收集有价值数据
                self.outputer.collect(new_datas)

                # 次数控制，希望爬一定次数就结束循环
                craw_times += 1
                if(craw_times >= 20):
                    break
            except:
                print("第%d次爬取出错了！！！" % craw_times)
        self.outputer.output() # 输出

# python默认的入口样式，__代表了系统默认变量
if __name__ == "__main__":
    # 入口网址，爬虫程序从这个网址开始爬取
    root_url = "https://baike.baidu.com/item/Python/407313"
    # 爬虫调度器类的对象，使用这个对象调用爬取的功能
    spider = Spider_Main()
    # 调用craw方法爬取网址
    spider.craw(root_url)
