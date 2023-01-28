import undetected_chromedriver as uc
import os,shutil
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

post_ = 137291
count_ = 1
error_ = 0
location_ = f'{os.getcwd()}/chapters'
# <!.... Open Browser ....!>
browser = uc.Chrome(use_subprocess=True)
for i in links:
    try:
        # <!... Get Data From Page ....!> 
        browser.get(i)
        browser.implicitly_wait(60)
        content = browser.find_element(By.XPATH, f'//*[@id="post-{post_}"]/div[2]/div/div[4]').text
        # <!... Save Data ....!> 
        with open(f'{location_}/chapter{count_}.txt','w',encoding="utf-8") as f:
            f.write(content)
        print(f'[!] Chapetr {count_} is Done Saved')
        count_ += 1
        post_ += 1
    except:
        with open('error.txt','a+') as file :
            file.write(f'Link For Chaper: {count_} Chapter Link : {i} \n')
        print(f'[!] Error For Chaper: {count_} Chapter Link : {i} ')
        count_ += 1
        post_ += 1


try:
    shutil.make_archive(rf'{location_}','zip', location_)
    print("zip success")
except Exception as e:
    print('Error')
