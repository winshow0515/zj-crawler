import requests
response = requests.get("https://zerojudge.tw/ShowProblem?problemid=q838")
print(f"Response Code: {response.status_code}")
response.content # 拿 bytes 
data = response.text # 拿 str
import re # Regular Expression

# for row in data.split('\n'):
#     if "<title>" in row:
#         title = row.strip()[7:-20]
title = re.findall("<title>(....).* - 高中生程式解題系統</title>", data)[0]
print("Problem title :", title)
problem_content = re.findall('<div id="problem_content" class="problembox"><p>(.*)</p>', data)[0]
import html
print("Problem Content :", html.unescape(problem_content))
S = "SA--AB-B---ABBAA0123abcX"
print(re.findall("A.*?(?:-A|B)", S))
print(re.findall("([0-9a-fA-F]{3,})", S))


url = "https://zh.wikipedia.org/wiki/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6"

response = requests.get(url)
