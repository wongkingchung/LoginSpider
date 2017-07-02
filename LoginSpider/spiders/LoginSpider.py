# -*- coding: utf-8 -*-
import scrapy
from LoginSpider.items import LoginspiderItem
from scrapy.spiders import BaseSpider
from scrapy.http import Request,FormRequest
from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException
from scrapy import Selector
from scrapy.http import TextResponse
import csv
import re

class LoginSpider(BaseSpider):
    name = 'loginspider'
    start_urls = ['https://ionline.alliedworldgroup.com.hk/eapp/login.jsp']
    login_page='https://ionline.alliedworldgroup.com.hk/eapp/login.jsp'
    main_page ='https://ionline.alliedworldgroup.com.hk/eapp/' 

    def __init__(self):
		self.driver = webdriver.Chrome("C:\Coding\Scrapy\chromedriver.exe")


 	
    def parse(self, response):
         items = LoginspiderItem()
         
         self.driver.get(response.url)
         username = self.driver.find_element_by_name("login_id")
         password = self.driver.find_element_by_name("password")

         username.send_keys("UICF1SUC")
         password.send_keys("Convoy168")
         self.driver.find_element_by_xpath("//input[@type='button']").click()
#         sleep(randint(3,5))

         self.driver.find_element_by_link_text('Travel').click()

         with open('C:/Coding/Scrapy/LoginSpider/LoginSpider/spiders/request.csv', 'rb') as f:

            
            for line in f.readlines(): 
                 array = line.split(',')
                 adultno = array[0]
                 childno = array[1]
                 roundtrip = array[2]
                 fmdd = array[3]
                 fmmm = array[4]
                 fmyyyy = array[5]
                 todd = array[6]
                 tomm = array[7]
                 toyyyy = array[8]
                 toyyyy = re.sub(r'[\n\r\t]*', '', toyyyy)
            
                 
#                 self.driver.find_element_by_link_text('Travel').click()
        #         sleep(randint(3,5))		 
#                 adultno = 2
#                 childno = 3
                 self.driver.find_element_by_name("num_ind").clear()
                 self.driver.find_element_by_name("num_ind").send_keys(adultno)
                 self.driver.find_element_by_name("num_child").clear()
                 self.driver.find_element_by_name("num_child").send_keys(childno)
                         
#                 self.driver.find_elements_by_css_selector("input[type='radio'][value='N']")[0].click()
                 self.driver.find_elements_by_css_selector("input[type='radio'][value='" + roundtrip +"']")[0].click()
                         
#                 fmdd = "1"
#                 fmmm = "8"
#                 fmyyyy = "2017"
#                 todd = "10"
#                 tomm = "8"
#                 toyyyy = "2017"


#                 sleep(randint(3,5)) 

#                 self.driver.find_element_by_name("trvl_comm_date_dd").send_keys(fmdd)
#                 self.driver.find_element_by_name("trvl_comm_date_mm").send_keys(fmmm)
#                 self.driver.find_element_by_name("trvl_comm_date_yyyy").send_keys(fmyyyy)
                 self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_dd']/option[@value='" + fmdd +"']").click()
                 self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_mm']/option[@value='" + fmmm +"']").click()
                 self.driver.find_element_by_xpath("//select[@name='trvl_comm_date_yyyy']/option[@value='" + fmyyyy +"']").click()

#                 sleep(randint(1,2))

                 
#                 self.driver.find_element_by_name("trvl_expy_date_dd").send_keys(todd)
#                 self.driver.find_element_by_name("trvl_expy_date_mm").send_keys(tomm)
#                 self.driver.find_element_by_name("trvl_expy_date_yyyy").send_keys(toyyyy)
                 self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_dd']/option[@value='" + todd +"']").click()
                 self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_mm']/option[@value='" + tomm +"']").click()
                 self.driver.find_element_by_xpath("//select[@name='trvl_expy_date_yyyy']/option[@value='" + toyyyy +"']").click()
                         
                 self.driver.find_element_by_link_text(' Quote ').click()

         #        yield Request(self.driver.current_url, callback=self.extract_price)
                 resp = TextResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
                 price = resp.xpath('.//span[@class="dollar"]/text()').extract()
                 items['price1'] = price[0]
                 items['price2'] = price[1]
                 print price
                 
                 sleep(randint(1,2)) 
                 self.driver.find_element_by_link_text(' Re-Quote ').click()

		 

    def extract_price(self, response):
         self.driver.get(response.url)
            
        
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

