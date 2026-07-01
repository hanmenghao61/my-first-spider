import requests
from bs4 import BeautifulSoup
import csv
import time # 用于设置等待时间，做个礼貌的爬虫

# 1. 创建并打开一个名叫 quotes.csv 的文件，准备写入数据
# encoding='utf-8-sig' 是为了防止 Excel 打开时中文乱码
with open('quotes.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    # 先写入表头（第一行）
    writer.writerow(['名言', '作者'])

    # 2. 设置我们要抓取的页数，这里设置抓取第 1 到第 3 页
    print("开始执行抓取任务...")
    for page in range(1, 4):
        # 巧妙利用 f-string 动态生成每一页的网址
        url = f"http://quotes.toscrape.com/page/{page}/"
        print(f"正在抓取第 {page} 页: {url}")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 3. 寻找数据块
        # 这次我们先找到包裹着整条数据的 <div class="quote">
        quote_blocks = soup.find_all("div", class_="quote")
        
        # 4. 从每个数据块中，分别提取名言和作者
        for block in quote_blocks:
            # 提取名言文本
            text = block.find("span", class_="text").text
            # 提取作者名字
            author = block.find("small", class_="author").text
            
            # 5. 把提取到的两个数据写进刚才打开的 CSV 文件里
            writer.writerow([text, author])
            
        # 6. 礼貌等待：每次抓完一页，让程序休息 1 秒钟
        # 这是一个非常好的习惯，防止对目标服务器造成太大压力
        time.sleep(1)

print("\n🎉 抓取完成！快去你的代码文件夹里找找 quotes.csv 吧！")