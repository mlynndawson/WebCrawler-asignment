from selenium import webdriver
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

#opens a browser using Chrome and uses the chromedrive.exe
browser = webdriver.Chrome(executable_path=r'C:/Users/Mariah Dawson/Downloads/chromedriver_win32/chromedriver.exe') 
url ="http://www.montmere.com/test.php"
browser.get(url)

#using the url finds the element where username and password box is located
username = browser.find_element_by_id("username") 
password = browser.find_element_by_id("password") 

#enters the password and username for website
username.send_keys("test")
password.send_keys("test")

#finds the login in button and clicks
submitButton = browser.find_element_by_xpath("//*[@id='login']/input[3]")
submitButton.click() 
browser.get("http://www.montmere.com/test.php")
#make a pause to allow table to load
time.sleep(3)

#saves the html in the logged in page
innerHTML = browser.execute_script("return document.body.innerHTML") 
print (innerHTML)

#start parsing the innerHTML to find certain aspects
soup = BeautifulSoup(innerHTML,"html.parser")

#isolating the area/table to webcrawl
table= soup.findAll("table",{"class":"table"})[0]
rows = table.findAll("tr")

#variable open and save to a file after webcrawl
csvFile = open("car_model.csv", "w")
writer = csv.writer(csvFile)

try:
	#loop through rows and find the data
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td','th']):
			csvRow.append(cell.get_text())
		writer.writerow(csvRow)
finally:
	csvFile.close()