from datetime import datetime
import time

from selenium import webdriver
from playsound import playsound
from webdriver_manager.chrome import ChromeDriverManager

search = True

chrome = webdriver.Chrome(ChromeDriverManager().install())
playsound("./se.wav")

while True:

    try:
        chrome.implicitly_wait(10);
        chrome.get("https://reserve.tokyodisneyresort.jp/ticket/search/")
        try:
            data = chrome.find_element_by_class_name("textalign").text
        except:
            try:
                data = chrome.find_element_by_class_name("data").text
            except:
                break

        print(data)

        if data.find("ただいまアクセスが集中しておりアクセスしにくい状態") != -1:
            print("System : 販売していない : " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            time.sleep(0.5)
        elif data.find("受取方法") != -1:
            print("System : 販売開始した可能性 : " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            break
            playsound("./se.wav")
        else:
            print("System : 販売していない : " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            time.sleep(0.5)
    except:
        print("System : ページ取得エラー : " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        time.sleep(0.5)
        break

print("System : 販売開始した可能性があるためプログラムを終了します")
for a in range(10):
    playsound("./se.wav")
    time.sleep(0.5)



