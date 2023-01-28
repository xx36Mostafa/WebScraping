import undetected_chromedriver as uc
import os,shutil
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# ==> Get Links For Chapter's <==
links = []
for i in range(1,201):
    if i < 10:
        links.append(f'https://novelsemperor.com/konoha-deliberately-lost-to-hinata-at-the-start-chapter-00{i}/')
    elif i < 100:
        links.append(f'https://novelsemperor.com/konoha-deliberately-lost-to-hinata-at-the-start-chapter-0{i}/')
    else:
        links.append(f'https://novelsemperor.com/konoha-deliberately-lost-to-hinata-at-the-start-chapter-{i}/')

 # <!.... Create Folder ....!> 
try:
    os.mkdir('chapters')
    print('[!] Done Create Folder')
except:
    pass

count_ = 1
error_ = 0
location_ = f'{os.getcwd()}/chapters'
chap_ = []
# <!.... Open Browser ....!>
browser = uc.Chrome(use_subprocess=True)
for i in links:
    try:
        browser.get(i)
        filter_ =BeautifulSoup(browser.page_source,'lxml')
        content = filter_.find("div",{"class":"epcontent entry-content"}).find_all("p")
        for con_ in range(len(content)):
            chap_.append(content[con_].text)
        # <!... Save Data ....!> 
        with open(f'{location_}/chapter{count_}.txt',"w", encoding="utf-8") as f:
            for char in chap_:
                    f.write(char+'\n')
        print(f'[!] Chapetr {count_} is Done Saved')
        count_ += 1
        chap_.clear()
    except:
        with open('error.txt','a+') as file :
            file.write(f'Link For Chaper: {count_} Chapter Link : {i} \n')
        print(f'[!] Error For Chaper: {count_} Chapter Link : {i} ')        
        count_ += 1
        chap_.clear()

try:
    shutil.make_archive(rf'{location_}','zip', location_)
    print("zip success")
except Exception as e:
    print('Error')
