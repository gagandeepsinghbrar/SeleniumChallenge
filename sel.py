from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pickle import load,dump
import os,time

# ___________________________________
# Initial Setup
# ___________________________________


#read data from the file
try:

    with open('facebook_db','rb') as readme:
        accumulated=load(readme)


except:
    # If unable to find data initialize it to empty one
    accumulated=[]



tries=10

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
#Email and password fields
username=driver.find_element_by_id("email")
password=driver.find_element_by_id("pass")

# Typing credentials and submitting the form ...

# username and password fetch from environment instead of source code
username.send_keys(os.environ.get("usernamefb"))
password.send_keys(os.environ.get('passfb'))
password.send_keys(Keys.RETURN)



# Post container




# ___________________________________
# Need to filter data and store it
# ___________________________________

while tries>0:
    posts = driver.find_elements_by_xpath(".//div[contains(@class, '_5pbx userContent _3576')]")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Time can be changed to wait for updates

    time.sleep(100)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # add new data
    for postText in posts:
        
        if postText.text not in accumulated:

            accumulated.append(postText.text)
            
    # Refresh the page
    driver.refresh()


    # wait 10 seconds


    tries=tries-1




# ________________________________________________________________________________________________________



# ______Write to the file_________

print("<><><><><  Data so far captured   ><><><>")
print(accumulated)
with open('facebook_db',"wb") as writeme:
   dump(accumulated,writeme)

