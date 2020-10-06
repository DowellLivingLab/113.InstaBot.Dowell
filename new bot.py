from selenium import webdriver #importing Webdriver
import os
import time #for giving time between actions
import csv #importing csv to read csv files
import numpy as np 
import cv2
from selenium.webdriver.chrome.options import Options  #importing Chromedriver options

class InstagramBot:
#Creating A class
    def __init__(self, username, password):
        """
        Args: 
        username:str:The user username ,
        password:str:Ther user password

        Attributes:selenium webdriver

        """
       
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com' #base Url to redirect
        self.tag_url = 'https://www.instagram.com/explore/tags'
        self.driver = webdriver.Chrome('./chromedriver.exe') #Chromedriver path
        
        

        self.login()
        


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(10)
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
                 

    def nav_user(self, user):
        time.sleep(5)
        self.driver.get('{}/{}/'.format(self.base_url, user))
        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div').get_attribute('aria-disabled') #to check there is story or not on profile
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
        self.driver.set_window_size(S('Width = 425'),S('Height = 1134')) # For taking ScreenShot of the Page (May need manual adjustment)                                                                                                                
        self.driver.find_element_by_tag_name('body').screenshot('web_screenshot.png') 

        #print("Not_Active : " + self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div').get_attribute('aria-disabled')) #if Fals means A story is present on profile at present time.
    

    def follow_user(self, user):
         self.nav_user(user)
         time.sleep(5)

         follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
         
         follow_button.click()

         time.sleep(5)

    def msg_user(self, user):
         self.nav_user(user)
         

         self.driver.find_element_by_css_selector("button")[0].click()
         #self.driver.find_element_by_css_selector("button")[0]
         time.sleep(5)
         #self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()

    def Unfollow_user(self, user):
         self.nav_user(user)
         time.sleep(5)

         self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/button').click()
         time.sleep(5)
         self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
         time.sleep(5)
         
          
         
         
         
    



    
   
    


if __name__ == '__main__':
    ig_bot = InstagramBot('Username here', 'Password here')

   # myfile = open('Xyz.csv')  #CSV file name here file should be in same directory
    #for x in myfile:
        
     #ig_bot.Unfollow_user(x) 
    ig_bot.nav_user('mr_black_flash')
    #ig_bot.follow_user(x)

    
time.sleep(10)    


   # ig_bot.msg_user('thomasgeorgedowell')
    
