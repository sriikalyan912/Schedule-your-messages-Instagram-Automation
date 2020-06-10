from selenium import webdriver
from time import sleep
from datetime import datetime

class bot():
    sent=True
    
    def __init__(self,user,pswd):
        
        self.driver = webdriver.Chrome( 'chromedriver.exe')
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pswd)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        sleep(2)
    def verify(self,code):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/button').click()
        sleep(2)
    def initial_steps(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(1)
    def Send_msg(self,msg,to):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        sleep(2)
        direct=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div')
        sleep(2)
        links=direct.find_elements_by_tag_name('a')
        
        
        for i in range(len(links)):
            if to in links[i].text:
                links[i].click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                print('msg sent')
                self.sent=False
                self.driver.close()
            
        def Home(self):
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[1]/div/a/svg').click()
            sleep(1)

        def Logout():
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button').click()
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[9]').click()
            sleep(1)
            self.driver.close()

date=input("Date(MM/DD/YY):\t")
time=input("Time(hr:min): \t")

user=input('User name: ')
pswd=input('Password: ')

msg=input('Meassage')
To=input('To(user inst ID): ')
while True:
    crt_time=datetime.now()
    #print(crt_time)
    if date == crt_time.strftime("%D") and time == crt_time.strftime("%H:%M"):
        break
       

Bot=bot(user,pswd)

V=input('Is you\'ve activated two-step verification ?  yes or no :\t')

if V=='yes' or V=='Yes' or V=='y' or V=='YES':
    code = input('Enter your verification code that sent to your mobile:\t')
    Bot.verify(code)

Bot.initial_steps()

Bot.Send_msg(msg,To)

while Bot.sent :
    Bot.Home()
    Bot.Send_msg(msg,To)
Bot.Home()
Bot.Logout()
    


