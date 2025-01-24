要递归保存这个网站及其所有章节，可以使用上述方法之一。以下是针对你提供的网址 https://diveintosystems.org/book/introduction.html 的详细操作方案：

方法一：使用 pywebcopy 保存所有章节

pywebcopy 支持保存完整网站及其链接资源。

示例代码：

from pywebcopy import save_website

# 目标网页 URL 和保存目录
url = "https://diveintosystems.org/book/introduction.html"
download_folder = "./dive_into_systems_book"

# 保存整个网站
kwargs = {
    'bypass_robots': True,    # 忽略 robots.txt 限制
    'project_name': 'dive_into_systems'
}
save_website(url, download_folder, **kwargs)

print("书籍网站保存成功！")

运行后，程序会递归保存该页面及其子页面（如章节目录中链接的内容），存储在 ./dive_into_systems_book 文件夹中。

方法二：使用 wget 递归保存

wget 可以通过命令递归下载网站所有内容。

示例代码：

import os

# 目标网页 URL
url = "https://diveintosystems.org/book/introduction.html"

# 保存文件夹
output_folder = "./dive_into_systems_book"

# wget 递归下载命令
command = (
    f"wget --recursive --no-clobber --page-requisites --html-extension "
    f"--convert-links --restrict-file-names=windows --domains diveintosystems.org "
    f"--no-parent -P {output_folder} {url}"
)

# 执行命令
os.system(command)

print("书籍网站保存成功！")

参数说明：
	•	--recursive：递归下载所有链接。
	•	--no-parent：仅下载该页面及子页面，不下载父目录内容。
	•	--domains diveintosystems.org：限制仅下载该域名内的内容。
	•	-P ./dive_into_systems_book：指定保存位置。

方法三：自定义爬虫（使用 requests 和 beautifulsoup4）

如果需要更多灵活性，比如只抓取特定章节或只抓取正文内容，可以编写一个定制爬虫。

示例代码：

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def save_page(url, output_folder):
    """保存单个网页内容"""
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(output_folder, exist_ok=True)

        # 保存 HTML 文件
        file_name = os.path.basename(urlparse(url).path) or "index.html"
        file_path = os.path.join(output_folder, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"已保存：{url}")
        return response.text
    else:
        print(f"无法访问：{url}")
        return None

def crawl(url, output_folder, base_url, depth=2):
    """递归爬取网页"""
    if depth == 0 or url in visited:
        return
    visited.add(url)

    html = save_page(url, output_folder)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", href=True):
        href = link["href"]
        full_url = urljoin(base_url, href)
        if base_url in full_url and full_url not in visited:
            crawl(full_url, output_folder, base_url, depth - 1)

# 调用爬取函数
start_url = "https://diveintosystems.org/book/introduction.html"
output_directory = "./dive_into_systems_book"
crawl(start_url, output_directory, "https://diveintosystems.org", depth=3)

	•	depth=3：递归深度，可以调整以控制爬取范围。
	•	base_url="https://diveintosystems.org"：确保只抓取书籍页面。

注意事项
	1.	尊重版权：确认网站的内容许可，确保你有权保存这些内容。
	2.	爬取频率：如果你用自定义爬虫，请避免过于频繁的请求，使用 time.sleep 限制速率。
	3.	校验完整性：保存后检查是否所有章节和资源（如图片、CSS）均已下载。

如果你不确定选择哪个方法，可以先尝试 pywebcopy 或 wget，它们简单快捷。若有特殊需求，考虑用自定义爬虫解决。