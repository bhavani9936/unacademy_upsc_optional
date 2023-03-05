import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *

class UPSC_Optional:
    def __init__(self, driver):
        self.driver = driver

    # 1st scenario
    def click_Got_It(self):
        got_It = self.driver.find_element(By.XPATH, "//button[@class='e1q9ftw5 aquilla-button button css-94wbnh-StyButton']")
        got_It.click()

    def install_page(self):
        page= self.driver.find_element(By.XPATH, "(//div[@class='desktop css-14z299t-ScreenWrapper ernuq4a5'])[4]")
        self.driver.execute_script("arguments[0].click();", page)



    def click_subscripiton(self):
        plans = self.driver.find_element(By.XPATH, "//*[text()='Subscription plan']")
        plans.click()

    def click_success_stories(self):
        success_Stories = self.driver.find_element(By.XPATH,"(//span[@class='highlighter css-152mcpq'])[6]")
        success_Stories.click()

    def click_educators(self):
        educators = self.driver.find_element(By.XPATH, "(//div[@class='css-9hlkmq-TabLabel e1qfn6d713'])[2]")
        educators.click()


    def click_store_new(self):
        store_New= self.driver.find_element(By.XPATH, "//*[text()='Check it out']")
        store_New.click()

    def click_batch(self):
        batch = self.driver.find_element(By.XPATH, "//*[text()='Batch']")
        batch.click()



