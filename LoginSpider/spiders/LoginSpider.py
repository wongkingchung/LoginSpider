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
#         sleep(randint(3,5))
		 
         self.driver.find_element_by_link_text('Travel').click()
#         sleep(randint(3,5))		 
         adultno = 2
         childno = 3
         self.driver.find_element_by_name("num_ind").send_keys(adultno)
         self.driver.find_element_by_name("num_child").send_keys(childno)
		 
         self.driver.find_elements_by_css_selector("input[type='radio'][value='N']")[0].click()
		 
         fmdd = "1"
         fmmm = "8"
         fmyyyy = "2017"
         todd = "10"
         tomm = "8"
         toyyyy = "2017"
#         self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_dd']/option[@value='" + fmdd +"']").click()
#         self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_mm']/option[@value='" + fmmm +"']").click()
#         self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_yyyy']/option[@value='" + fmyyyy +"']").click()
         
##         self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_dd']/option[@value='" + todd +"']").click()
#         self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_mm']/option[@value='" + tomm +"']").click()
#         self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_yyyy']/option[@value='" + toyyyy +"']").click()

         self.driver.find_element_by_name("trvl_comm_date_dd").send_keys(fmdd)
         self.driver.find_element_by_name("trvl_comm_date_mm").send_keys(fmmm)
         self.driver.find_element_by_name("trvl_comm_date_yyyy").send_keys(fmyyyy)
         self.driver.find_element_by_name("trvl_expy_date_dd").send_keys(todd)
         self.driver.find_element_by_name("trvl_expy_date_mm").send_keys(tomm)
         self.driver.find_element_by_name("trvl_expy_date_yyyy").send_keys(toyyyy)
		 
         self.driver.find_element_by_link_text(' Quote ').click()
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

