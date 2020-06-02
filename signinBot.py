import eel
from selenium import webdriver
import time
import schedule
from datetime import datetime


eel.init('UIElements')

##
@eel.expose
class letTheBotOut:
    def __init__(self, username, pswd):
        ###########################################################################################################################
        ########    For manual usage Enter Target Information here   ##############################################################
        ###########################################################################################################################
        #url of the login page
        URL = 'YOUR_URL'
        #Xpath of the username field
        USERNAMEXPATH = 'YOUR_XPATH_OF_THE_USERNAME_BUTTON'
        #Xpath of the password field
        PASSWORDXPATH = 'YOUR_XPATH_OF_THE_PASSWORD_BUTTON'
        #Xpath of the loginbutton
        LOGINXPATH = 'YOUR_XPATH_OF_THE_LOGIN_BUTTON'
        #url of the target page
        TARGETURL = 'YOUR_URL_OF_THE_FINAL_TARGET_PAGE'
        #Xpath of the Target
        TARGETXPATH = 'YOUR_XPATH_OF_THE_TARGET'
        ###########################################################################################################################
        ###########################################################################################################################

        self.driver = webdriver.Safari()
        self.driver.get(URL)
        time.sleep(2)
        self.driver.find_element_by_xpath(USERNAMEXPATH).send_keys(username)
        self.driver.find_element_by_xpath(PASSWORDXPATH).send_keys(pswd)
        #login
        self.driver.find_element_by_xpath(LOGINXPATH).click()
        #sleep(4)
        #go to target page
        self.driver.get(TARGETURL)
        #sleep(2)
        #hit target
        self.driver.find_element_by_xpath(TARGETXPATH).click()


###########################################################################################################################
##########  For manual usage Enter Login Details and Time here   ##########################################################
###########################################################################################################################
#time
TIME = 'YOUR_TIME_E.G._"19:30"'
#username
USERNAME = 'YOUR_USERNAME'
#password
PASSWORD = 'YOUR_PASSWORD'
###########################################################################################################################
###########################################################################################################################


schedule.every().day.at(TIME).do(letTheBotOut(USERNAME, PASSWORD))


while True:
    schedule.run_pending()
    time.sleep(1)

###########################################################################################################################
###########################################   CHANGE | TO YOUR BROWSER (e.g. 'firefox', 'chrome', 'edge' etc.) ############
#                                                    V
eel.start('index.html', size={1000, 600}, mode = 'safari') 

###########################################################################################################################
###########################################################################################################################
