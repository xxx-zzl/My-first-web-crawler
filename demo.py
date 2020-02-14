# 请求网页
import requests    # 调用requests
import re          # 调用正则模块
import time        # 调用时间模块
import os          # 调用os模块
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
}    # 请求头信息
y = [1, 2, 3, 4, 5, 6, 7]    # 手动找到7个列表  待优化
for x in y:
    xx = 'https://www.vmgirls.com/13344/page-'+str(x)+'.html'


    response = requests.get(xx,headers=headers)
    # print(response.request.headers)
    html = response.text

    # 解析网页
    dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]   # 提取标题
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)                                                    # 判断如果没有就创建一个以标题为名的文件夹
    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    print(urls)  # 输出所有url

    # 保存图片
    for url in urls:
        time.sleep(1)
        file_name = url.split('/')[-1]         # 提前图片名
        response = requests.get(url, headers=headers)
        # 二进制文件写入
        with open(dir_name + '/' + file_name, 'wb') as f:
            f.write(response.content)
