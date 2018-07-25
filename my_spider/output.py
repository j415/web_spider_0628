# coding: utf-8
# 版权所有：该文件第一版权人为王振中（298046805）
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect(self, new_datas):
        if new_datas is None:
            return
        self.datas.append(new_datas)

    # 将爬取到的数据写成HTML页面
    def output(self):
        file_out = open("output.html","w", encoding="utf-8")
        file_out.write("<html>")
        file_out.write("<body>")
        file_out.write("<table>")

        for data in self.datas:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['url'])
            file_out.write("<td>%s</td>" % data['title'])
            file_out.write("<td>%s</td>" % data['summary'])
            file_out.write("</tr>")

        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()