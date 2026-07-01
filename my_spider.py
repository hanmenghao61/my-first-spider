import requests
from bs4 import BeautifulSoup
import os
import csv
import time

# 1. 初始化准备：创建图片文件夹
image_folder = "gallery_images"
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

# 2. 创建并准备好我们的“图文总账本” CSV 文件
with open('illustrated_quotes.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    # 表头增加了【配图本地路径】这一列，实现图文关联
    writer.writerow(['名言内容', '作者', '艺术配图路径'])

    print("第一步：正在前往名言网站抓取文字...")
    # 抓取 5 条名言
    quote_url = "http://quotes.toscrape.com/"
    quote_res = requests.get(quote_url)
    quote_soup = BeautifulSoup(quote_res.text, "html.parser")
    quote_blocks = quote_soup.find_all("div", class_="quote")[:5]

    print("第二步：正在前往书城网站抓取艺术背景图...")
    # 抓取 5 张图书封面作为配图
    book_url = "http://books.toscrape.com/"
    book_res = requests.get(book_url)
    book_soup = BeautifulSoup(book_res.text, "html.parser")
    book_blocks = book_soup.find_all("article", class_="product_pod")[:5]

    print("第三步：开始进行图文配对与下载...")
    
    # 💡 核心魔法：使用 zip() 函数让名言和图片“齐头并进”一一配对
    for i, (quote_block, book_block) in enumerate(zip(quote_blocks, book_blocks), start=1):
        # 提取名言和作者
        text = quote_block.find("span", class_="text").text
        author = quote_block.find("small", class_="author").text
        
        # 提取并拼接图片链接
        img_tag = book_block.find("img")
        img_url_relative = img_tag.get("src")
        img_url_full = "http://books.toscrape.com/" + img_url_relative
        
        # 制定图片的保存名字，比如 "gallery_images/bg_1.jpg"
        image_name = f"bg_{i}.jpg"
        local_image_path = f"{image_folder}/{image_name}"
        
        # 下载图片并保存
        print(f" 正在下载第 {i} 组配图...")
        img_data = requests.get(img_url_full).content
        with open(local_image_path, "wb") as img_file:
            img_file.write(img_data)
            
        # 关键的一步：把【文字数据】和【图片在电脑里的路径】一起写进表格
        writer.writerow([text, author, local_image_path])
        
        # 礼貌等待
        time.sleep(1)

print("\n🎉 项目大成功！")
print("1. 【图片】已全部存入 gallery_images 文件夹")
print("2. 【图文账本】已写入 illustrated_quotes.csv，快用 Excel 打开看看吧！")