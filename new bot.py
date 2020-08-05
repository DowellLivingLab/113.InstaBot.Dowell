from selenium import webdriver
#import webdriver from selenium (To access the web browser)
import os
import time
import csv

class InstagramBot:

    def __init__(self, username, password):
        """
        Args: 
        username:str:The user username ,
        password:str:Ther user password

        Attributes:selenium webdriver

        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.tag_url = 'https://www.instagram.com/explore/tags'
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()
        


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(10)
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
                 
        time.sleep(5)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))


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
         
          
         
         
         


    def nav_tag(self,tag):
        self.driver.get('{}/{}/'.format(self.tag_url, tag))
        #self.driver.get('https://www.instagram.com/explore/tags/' + hashtag+ '/cat')
        time.sleep(5)


    
   
    


if __name__ == '__main__':
    ig_bot = InstagramBot('Username', 'Password')
    #write your instagram username in 'Username'
    #write your intagram password in 'Password'


    myfile = open('Searchmybio.csv')
    for x in myfile:
    #target = myfile.readline(i)
     time.sleep(60)
     ig_bot.follow_user(x)
    
   # ig_bot.nav_user('pooja_srivastava_22')
   # ig_bot.nav_tag('food')
   # ig_bot.msg_user('thomasgeorgedowell')
