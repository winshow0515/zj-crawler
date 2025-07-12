import requests
import html

response = requests.get("https://zerojudge.tw/ShowProblem?problemid=a024")
print(f"Response Code: {response.status_code}")
response.content # 拿 bytes 
data = response.text # 拿 str

import re # Regular Expression

#q838. 3. 貪心闖關
title = re.findall("<title>(.*) - 高中生程式解題系統</title>", data)[0]
print("Problem title :", title)

#題目標籤、通過比率、評分方式、最近更新時間
problem_infor = html.unescape(re.findall('<div class="col-md-4">(.*?)</div>', data, re.DOTALL))[0]
#print("Problem Information :\n", html.unescape(problem_infor))

#題目標籤
problem_tags = re.findall('<span class="tag">(.*?)</span>', problem_infor, re.DOTALL)[0].strip()
problem_tags = re.sub(r'<a.*?>|</a>', '', problem_tags).split()  # 移除 <a> 標籤
print("Problem Tags :", problem_tags)


#通過比率
# 原始抓到的是整段 <span title="解題統計">...</span> 的內容（含兩個 <a>）
submission_html = re.findall(r'<span title="解題統計">(.*?)</span>', problem_infor, re.DOTALL)[0]
# 從中抓出所有 <a>...</a>
submission_links = re.findall('<a .*?>(.*?)</a>', submission_html, re.DOTALL)
print(submission_links)
# 解碼 & 去除空白
submission_links = [html.unescape(x).strip() for x in submission_links]

print("Problem Submission 人數：")
print("通過人數：", submission_links[0])   # 例如：36087人
print("嘗試人數：", submission_links[1])   # 例如：38982人


#內容
div_problem_content = re.findall('<div id="problem_content" class="problembox">(.*?)</div>', data,re.DOTALL)[0]
paragraphs = re.findall('<p>(.*?)</p>', div_problem_content, re.DOTALL)
print("Problem Content :")
for i, paragraph in enumerate(paragraphs):
    paragraphs[i] = html.unescape(paragraph.strip()).replace("<br>", "\n").replace("<br />", "\n")
    print(paragraphs[i])


