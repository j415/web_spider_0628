# coding: utf-8
# 版权所有：该文件第一版权人为王振中（298046805）
import urllib.request as my_reqrequest

class UrlDownloader(object):
    # 通过网址下载网页，本次使用的是Python 3.0自带的下载器类库urllib.request
    def download(self, current_url):
        # return my_reqrequest.urlopen(current_url).read()
        # 由于网页编码格式问题，通常需要在下载或者解析时
        # 通过decode或者encode进行转码
        return my_reqrequest.urlopen(current_url).read().decode("utf-8")