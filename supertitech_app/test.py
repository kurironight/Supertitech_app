from selenium import webdriver
import csv  
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='c:\\selenium\\chromedriver.exe')  # 今は chrome_options= ではなく options=
driver.get('http://www.ocw.titech.ac.jp/index.php?module=General&action=T0200&GakubuCD=4&GakkaCD=342300&KeiCD=23&tab=2&focus=200&lang=JA')
tablelist = driver.find_elements_by_css_selector("table.ranking-list tbody tr")

subject_url = []
title_list = []

def subjects_to_DataFrame(subject_list):
    for subject in subject_list:
        subject[5] = subject[5][0]
    return pd.DataFrame(subject_list, columns=['title', 'teacher', 'time', 'code', 'credit', 'Q', 'content'])

# とりあえず各subjectのURLだけ取得
for item in tablelist:
    url = item.find_element_by_css_selector('td.course_title a').get_attribute('href')
    title = item.find_element_by_css_selector("td.course_title a").text
    title_list.append(title)
    subject_url.append(url)

print('subjects:' + str(len(subject_url)))
subjectlist = []
for i,url in enumerate(subject_url):
    # 格URLにアクセスして情報を取得
    driver.get(url)
    teacher = driver.find_element_by_css_selector("dl.clearfix a").text
    time = driver.find_element_by_css_selector("dd.place").text
    datalist = driver.find_elements_by_css_selector("dl.dl-para-l dd")
    content = driver.find_element_by_css_selector("div.cont-sec p").text
    code = datalist[0].text
    credit = datalist[1].text
    Q = datalist[3].text
    subject = [title_list[i], teacher, time, code, credit, Q, content]
    print(subject)
    subjectlist.append(subject)

for item in subjectlist:
    print(item)

df = subjects_to_DataFrame(subjectlist)
df.to_csv('output.csv')
#search_box = driver.find_element_by_name("q")
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#print(driver.title)​
#driver.save_screenshot('search_results.png')
driver.quit()