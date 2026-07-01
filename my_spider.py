import requests
from bs4 import BeautifulSoup
import os  # 新朋友：用于操作系统的文件和文件夹管理
import time

# 1. 自动创建一个叫 "book_covers" 的文件夹来存放图片
folder_name = "book_covers"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"📁 成功创建文件夹: {folder_name}")

# 2. 目标网站（专门用来练手的沙盒书城）
url = "http://books.toscrape.com/"
print("正在访问书城首页...")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 3. 找到包含图书信息的模块 
# 在这个网站里，每本书的信息都被包裹在一个叫 <article class="product_pod"> 的标签里
books = soup.find_all("article", class_="product_pod")

print("🚀 开始下载图片...")

# 4. 为了测试，我们先抓取前 5 本书 (books[:5])
for book in books[:5]:
    # 找到 <img> 标签
    img_tag = book.find("img")
    
    # 提取书名（用作图片的文件名），它存在 alt 属性中
    title = img_tag.get("alt")
    # 简单清洗一下文件名，防止书名里有特殊标点符号导致电脑保存文件失败
    safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    
    # 提取图片的相对链接 (存放在 src 属性中，比如 "media/cache/...")
    img_url_relative = img_tag.get("src")
    
    # ⚠️ 关键步骤：拼接成完整的、能在浏览器里直接打开的图片下载链接
    img_url_full = "http://books.toscrape.com/" + img_url_relative
    
    print(f"正在下载: {safe_title}.jpg")
    
    # 5. 向图片的完整链接发送请求，获取图片的二进制数据
    img_response = requests.get(img_url_full)
    
    # 6. 保存图片文件
    # 拼接出保存路径，比如 "book_covers/A Light in the Attic.jpg"
    file_path = f"{folder_name}/{safe_title}.jpg"
    
    # 'wb' 的意思是 Write Binary（写入二进制），这是保存图片/音频/视频的关键模式！
    with open(file_path, "wb") as file:
        # img_response.content 获取到的就是图片的二进制原始数据
        file.write(img_response.content)
        
    # 礼貌等待 1 秒，保护对方服务器
    time.sleep(1)

print(f"\n🎉 下载完成！快去你的代码目录下，打开 【{folder_name}】 文件夹看看吧！")