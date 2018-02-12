import requests
import time
import os
from pygame import mixer
while(True):
    page=requests.get('http://www.vce.ac.in/COE.aspx')
    data=page.text
    if data.count("01-2018")==1:
        time.sleep(120)
        print("No")
        continue
    else:
        flag=1
        break
if flag==1:
    os.system('C:\\Users\\Vineeth\\AppData\\Local\\Programs\\Python\\Python35-32\\python sms.py')
    mixer.init()
    mixer.music.load('D:\Songs\English\Others\Summer.mp3')
    mixer.music.play()
    
    
