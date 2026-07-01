# 🖼️ 图文名言珍藏馆 (Illustrated Quotes Scraper)

这是一个适合零基础入门的 Python 爬虫实战项目。它能够自动从网页上抓取名言金句，并与精美的图书封面进行图文配对，最终生成一份包含图片路径的本地 CSV 档案。

## ✨ 项目功能
* **文本抓取**：自动抓取目标网站的名言文字和作者。
* **媒体下载**：自动抓取目标网站的图书封面图片，并下载保存到本地 `gallery_images` 文件夹。
* **图文关联**：使用 Python 的 `zip()` 函数将文字与图片精准配对，最终导出关联好的 `illustrated_quotes.csv`。

## 🛠️ 技术栈
* **开发语言**：Python 3
* **核心工具库**：
  * `requests`：负责发送网络请求，获取网页源代码及图片二进制流。
  * `BeautifulSoup4`：负责解析 HTML 结构，精准定位目标数据。
  * `csv` & `os`：负责本地文件系统的操作与表格导出。

## 🚀 如何运行

1. 下载或克隆本项目到本地：
```bash
git clone [https://github.com/hanmenghao61/my-first-spider.git](https://github.com/hanmenghao61/my-first-spider.git)
安装必备的第三方依赖库：

Bash
pip install requests beautifulsoup4
运行主爬虫脚本：

Bash
python my_spider.py
⚠️ 免责声明
本项目仅作 Python 爬虫技术学习与交流使用，抓取目标均为专门提供给新手的开源沙盒测试网站（toscrape.com）。