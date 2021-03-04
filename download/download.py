import urllib.request
import sys
import os
sys.path.append(os.getcwd())
from parse import zhongheng
# sys.path.append("../../")
# from qq import add
# from qq.add import parse_book_details

def download():
    # response = urllib.request.urlopen("http://book.zongheng.com/book/1103020.html") # 书籍首页
    response = urllib.request.urlopen("http://home.zongheng.com/show/userInfo/52486753.html")
    html = response.read().decode("utf8")
    print(html)


if __name__ == "__main__":
    # zhongheng.ParseZhongheng().parse_book_details(html)
    # print("执行了")
    # download()
    pass
