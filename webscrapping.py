# The wget, BeautifulSoup and selenium modules
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def webcontent(url):  
    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    # driver = webdriver.Chrome('G:\Softwares\chromedriver.exe') | Chrome() with Firefox()   
    # use PhantomJS and stop the browser from popping up,
    driver.get("https://www.whois.com/") # load the web page
    elem = driver.find_element_by_id("whois_search_input") 
    elem.send_keys(url)
    elem.send_keys(Keys.RETURN) 
    page="https://www.whois.com/whois/"+url
    driver.get(page)
    src = driver.page_source
    parser = BeautifulSoup(src,"lxml") # initialize the parser and parse the source "src"
    list_of_attributes = {"class" : "df-raw", "id" : "registrarData"} # A list of attributes 
    tag = parser.findAll('pre',attrs=list_of_attributes)
    tag=str(tag).split('\n')
    driver.close()
    return tag

#tag = webcontent("google.com")
#for i in range(0,5):
#print(tag[5])
