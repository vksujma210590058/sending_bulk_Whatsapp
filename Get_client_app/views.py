from django.shortcuts import render


from selenium.webdriver.chrome.options import Options

import pandas as pd
options=Options()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=1000 --user-data-dir=C:\Users\vksuj\chrome_data



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:1000")

service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)

def send_message_via_whatsapp(phone_numbers,messages):

    driver.get("https://web.whatsapp.com/")
    time.sleep(16)
    try:
        for phone_number,message in zip(phone_numbers,messages):
            driver.find_element(By.XPATH,'//div[@title="New chat"]').click()
            driver.find_element(By.XPATH,'//div[@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]').send_keys(phone_number)
            actions = ActionChains(driver)
            time.sleep(1.5)
            try:
                driver.find_element(By.XPATH,'//span[contains(text(), "No results found for")]')
                driver.find_element(By.XPATH,'//div[@aria-label="Back"]').click()
                time.sleep(.5)
            except:

                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(.5)

                driver.find_element(By.XPATH,'//div[@aria-placeholder="Type a message"]').send_keys(message)
                try:
                    driver.find_element(By.XPATH,'//button[@aria-label="Send"]').click()
                    time.sleep(.5)
                except:
                    pass
                print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"An error occurred: {e}")




def home (request):


    if request.method == 'POST':
        form_id = request.POST.get('form_id')



        if form_id=="form3":
            excel_file_path3 = request.POST.get('excel_file_path3')


            df=pd.read_excel(fr"{excel_file_path3}")
            phone_numbers=df.iloc[:,0].to_list()
            messages=df.iloc[:,1].to_list()

            send_message_via_whatsapp(phone_numbers=phone_numbers,messages=messages)




    return render(request, 'home.html',)

