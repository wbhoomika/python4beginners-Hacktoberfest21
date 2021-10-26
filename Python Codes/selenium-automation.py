# Automating the process of checking internet speed and tweeting a complaint on twitter

from selenium import webdriver
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 50
CHROME_DRIVER_PATH = '###CHROMEDRIVER PATH####'
TWITTER_EMAIL = '###EMAIL###'
TWITTER_PASSWORD = '###PASSWORD####'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.maximize_window()
        self.go = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go.click()
        print("clicked")
        sleep(50)
        self.down = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print("Down:", self.down)
        print("UP:", self.up)
        self.message = f"Hey Internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                       f" {PROMISED_DOWN}down/{PROMISED_UP}up?"

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        sleep(1)
        username = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        button.click()
        sleep(2)
        write_here = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        write_here.send_keys(self.message)
        tweet = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet.click()
        print("Tweeted Successfully!")


complain_bot = InternetSpeedTwitterBot()
complain_bot.get_internet_speed()
complain_bot.tweet_at_provider()
