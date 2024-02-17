import Resources
import webbrowser
from time import sleep
from urllib.parse import quote
import pyautogui

customers = Resources.customer_list

for customer in customers:

    customer_name = customer[0]
    customer_phone = customer[1]

    message = f'Hi! {customer_name}, how are you?' #write here your message
    whatsapp_link = f'https://web.whatsapp.com/send?phone={customer_phone}&text={quote(message)}'

    webbrowser.open(whatsapp_link) #you need to be logged in to whatsapp web
    sleep(10) #adjust this time according to your internet speed to open whatsapp web
    button = pyautogui.locateCenterOnScreen(r'Assets\button.png') #pyautogui searches by the image on screen, so don't obstruct the button
    sleep(5)
    pyautogui.click(button[0], button[1])
    pyautogui.hotkey('ctrl', 'w')



