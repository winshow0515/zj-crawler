import requests
import html
import re # Regular Expression
response = requests.get("https://zerojudge.tw/ShowProblem?problemid=q838")
print(f"Response Code: {response.status_code}")
response.content # 拿 bytes 
data = response.text # 拿 str



#q838. 3. 貪心闖關
title = re.findall(r'<title>(.*) - 高中生程式解題系統</title>', data)[0]
print("Problem title :", title)


problem_infor = re.findall(r'<div class="col-md-4">(.*?</div>.*?)</div>', data, re.DOTALL)[0]
print("Problem Information :\n", problem_infor)

#題目標籤
problem_tags = re.findall(r'<span class="tag">(.*?)</span>', problem_infor, re.DOTALL)[0].strip()
problem_tags = re.sub(r'<a.*?>|</a>', '', problem_tags).split()  # 移除 <a> 標籤
print("Problem Tags :", problem_tags)


#通過比率
# 原始抓到的是整段 <span title="解題統計">...</span> 的內容（含兩個 <a>）
submission_html = re.findall(r'<span title="解題統計">(.*?)</span>', problem_infor, re.DOTALL)[0]
submission_links = re.findall(r'<a .*?>(.*?)</a>', submission_html, re.DOTALL)
percent_text = re.findall(r'\d+%', submission_html, re.DOTALL)[0].strip()
print("Problem Submission 人數：")
print("通過人數：", submission_links[0])   # 例如：36087人
print("嘗試人數：", submission_links[1])   # 例如：38982人
print("通過率：", percent_text)  # 例如：92.1%


#評分方式
Scoring_method = re.findall(r'<div class="btn btn-warning btn-xs">(.*?)</div>', problem_infor, re.DOTALL)[0]
print("Problem Scoring Method :", Scoring_method)


#最近更新
print("Problem Last Updated :", re.findall(r'<br /> 最近更新 :(.*?)<br />', problem_infor, re.DOTALL)[0].strip())


#內容
div_problem_content = re.findall(r'<div id="problem_content" class="problembox">(.*?)</div>', data,re.DOTALL)[0]
paragraphs = re.findall(r'<p>(.*?)</p>', div_problem_content, re.DOTALL)
print("Problem Content :")
for i, paragraph in enumerate(paragraphs):
    paragraphs[i] = html.unescape(paragraph.strip()).replace("<br>", "\n").replace("<br />", "\n")
    print(paragraphs[i])


#輸入說明
problem_theinput = re.findall(r'<div id="problem_theinput" class="problembox">(.*?)</div>', data,re.DOTALL)[0]
paragraphs = re.findall(r'<p>(.*?)</p>', problem_theinput, re.DOTALL)
print("輸入說明 :")
for i, paragraph in enumerate(paragraphs):
    paragraphs[i] = html.unescape(paragraph.strip()).replace("<br>", "\n").replace("<br />", "\n")
    print(paragraphs[i])

#輸出說明
problem_theoutput = re.findall(r'<div id="problem_theoutput" class="problembox">(.*?)</div>', data,re.DOTALL)[0]
paragraphs = re.findall(r'<p>(.*?)</p>', problem_theoutput, re.DOTALL)
print("輸出說明 :")
for i, paragraph in enumerate(paragraphs):
    paragraphs[i] = html.unescape(paragraph.strip()).replace("<br>", "\n").replace("<br />", "\n")
    print(paragraphs[i])


#範例輸入
input_example = re.findall(r'<div class="panel-heading">範例輸入(.*?)</div>', data, re.DOTALL)
print("範例輸入 :", input_example)#為什麼又是空串列？？？