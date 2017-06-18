import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import Request,FormRequest
from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException


class LoginSpider(BaseSpider):
    name = 'loginspider'
    start_urls = ['https://ionline.alliedworldgroup.com.hk/eapp/login.jsp']
    login_page='https://ionline.alliedworldgroup.com.hk/eapp/login.jsp'

    def __init__(self):
		self.driver = webdriver.Chrome("C:\Coding\Scrapy\chromedriver.exe")

	
    def parse(self, response):
#        return [FormRequest.from_response(response,
#                    formdata={'login_id': 'UICF1SUC', 'password': 'Convoy168'},
#                    callback=self.after_login)]
         self.driver.get(response.url)
         username = self.driver.find_element_by_name("login_id")
         password = self.driver.find_element_by_name("password")

         username.send_keys("UICF1SUC")
         password.send_keys("Convoy168")
         self.driver.find_element_by_xpath("//input[@type='button']").click()
         sleep(randint(3,5))
		 
         self.driver.find_element_by_link_text('Travel').click()
         sleep(randint(3,5))		 
         adultno = 2
         childno = 3
         self.driver.find_element_by_name("num_ind").send_keys(adultno)
         self.driver.find_element_by_name("num_child").send_keys(childno)
         sleep(randint(3,5))
		 
					
    def after_login(self, response):
        # check login succeed before going on
		
        if "UICF1SUC" in response.body:
            print 'logged in Allied World'
            print response.url
            self.driver.get(response.url)
			
            try:
                travellnk = self.driver.find_element_by_link_text('Travel').click()
            except NoSuchElementException:
                pass
			# insert how you want to handle this e.g. break, log etc

 
			
			
        else:
            print 'not logged in'
        return

