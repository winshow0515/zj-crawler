import requests
import html
import re # Regular Expression
response = requests.get("https://zerojudge.tw/ShowProblem?problemid=j608")
print(f"Response Code: {response.status_code}")
response.content # 拿 bytes 
data = response.text # 拿 str

#q838. 3. 貪心闖關
title = re.findall(r'<title>(.*) - 高中生程式解題系統</title>', data)[0]
print("Problem title :", title)


problem_infor = re.findall(r'<div class="col-md-4">(.*?</div>.*?)</div>', data, re.DOTALL)[0]
#print("Problem Information :\n", problem_infor)

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

print("\n---\n")

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

print("\n---\n")

example_case = re.findall(r'<div class="problembox">.*?<pre>(.*?)</pre>', data, re.DOTALL)
#print(example_case)
for i in range(0, len(example_case), 2):
    print(f"範例測資 {i//2+1}")
    print(f"Input:")
    print(example_case[i].strip())
    print(f"Output :")
    print(example_case[i+1].strip())

print("\n---\n")

case_info = re.findall(r'<div class="panel panel-default">.*?<div class="panel-heading">測資資訊：</div>.*?<div class="panel-body">(.*?)</div', data, re.DOTALL)[0]
case_info = re.sub(r'\t', '', html.unescape(case_info))
case_info = re.sub(r'<br />', '', case_info)
case_info = case_info.split()


fmt = "| {: <4s} | {: <10s} | {: <8s} | {: <8s} | {: <6s} |"
print(case_info[0],case_info[1],case_info[2])
print(fmt.format("是否公開", "編號", "配分", "時間限制", "記憶體限制"))
print(fmt.format("-"*4, "-"*10, "-"*8, "-"*8, "-"*6))
for i in range(3, len(case_info), 6):
    print(fmt.format(case_info[i],case_info[i+1],case_info[i+2],case_info[i+3],case_info[i+5]))

print("\n---\n")

div_problem_hint = re.findall(r'<div id="problem_hint" class="problembox">(.*?)</div>', data, re.DOTALL)[0]

problem_hint = re.findall(r'<p>(.*?)</p>', div_problem_hint, re.DOTALL)
print('problem hint:')
for text in problem_hint:
    print(html.unescape(re.sub(r'<br />', '\n', text)))
problem_tags = re.findall(r'<span class="tag">(.*?)</span>', data, re.DOTALL)[1].strip()
problem_tags = re.sub(r'<a.*?>|</a>', '', problem_tags).split()  # 移除 <a> 標籤
reference = re.findall(r'<span id="reference">(.*?)</span>', data, re.DOTALL)[0]
reference = re.findall(r'<a.*?>(.*?)</a>', reference, re.DOTALL)
manager = re.findall(r'<span style="display: inline-block;">(.*?)</div>', data, re.DOTALL)[0]
manager_email = re.findall(r'<a.*?title="(.*?)"', manager, re.DOTALL)[0]
manager_name = re.findall(r'<span title=.*?>(.*?)</span>', manager, re.DOTALL)[0]
print("reference :",reference)
print('manager : ', manager_email, manager_name)
print("Problem Tags :", problem_tags)
print("\n---\n")

#解題報告
print("解題報告：")
tbody = re.findall('<tr>(.*?)</tr>', data, re.DOTALL)


fmt2 = "| {: <5s} | {: <30s} | {: <20s} | {: <4s} | {: <64s} | {: <5} | {: <16} |"

if '<div align="center">' in tbody[1]:    #判斷是否有解題報告
    print('沒有發現任何「解題報告」')
else:
    # 每個tr底下有6個td，分別是 [編號,身分,題目,主題,人氣,發表日期]
    print(fmt2.format("編號", "身分", "姓名", "題目ID", "文章標題", "人氣", "發表日期"))
    print(fmt2.format("-"*5, "-"*30, "-"*20, "-"*4, "-"*64, "-"*5, "-"*16))
    for i in tbody[1:]:
        tr = re.findall(r'<td.*?>(.*?)</td>', i, re.DOTALL)
        number = tr[0].strip()
        email = re.findall(r'<a.*?title="(.*?)"', tr[1], re.DOTALL)[0]
        name = re.findall(r'<span title=.*?>(.*?)</span>', tr[1], re.DOTALL)[0]
        problem_id = re.findall(r'<a .*?>(.*?)</a>', tr[2], re.DOTALL)[0]
        articletitle = re.findall(r'<a .*?>(.*?)</a>', tr[3], re.DOTALL)[0]
        popularity = tr[4].strip()
        time = tr[5].strip()
        print(fmt2.format(number, email, name, problem_id, articletitle, popularity, time))
