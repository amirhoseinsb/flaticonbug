import pyperclip
import webbrowser
import bs4
import requests
import time




while True : #Check Internet Connection 

    flatIconUrl = requests.get("http://flaticon.com") # Url
    check_Status = (flatIconUrl.status_code)# Responce Status

    if check_Status == 200 : # Check 1
        print("\n\n\n ***Internet access status: OK***")
        break
    elif check_Status != 200: # Check 2
        print("""\n\n***ERROR***

1 - Please check your internet connection 
2 - Check The Vpn Connection
        """)

        time.sleep(15) # 15 seconds Stop

        flatIconUrl2 = requests.get("http://flaticon.com")# Url
        check_Status_2 = (flatIconUrl2.status_code) # Responce Status

        if check_Status_2 == 200 :# Check 3
            break

print("\n Welcome To The Software : Please Copy the Image!") # welcome

while True :

        list = []

        if pyperclip.waitForNewPaste() != 'None':

            value = pyperclip.paste()
            list.append(value)
            req = list[0]
            print(f"\n{req}")


            if "icon" in req:
                r = requests.get(req)
                print(f"\n responce status is : {r}")
                page = r.text
                soup = bs4.BeautifulSoup(page,"html.parser")

                for link in soup.find_all("div", "main-icon-without-slide pd-lv4 icon-png-container"):
                    image = (link.get('data-png'))
                    webbrowser.open_new_tab(image)
            else :
                print(" ")
