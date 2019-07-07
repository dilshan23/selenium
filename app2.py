from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#we can put functions like login,like functions insie a class
class FbBot:
	def __init__(self,username,password):  #constructor function
		self.username = username
		self.password = password
		
		#self.query = query
		self.bot = webdriver.Chrome(chromedriver)

		#  new metho on this class

	def login(self):
		bot = self.bot
		bot.get('https://facebook.com')
		time.sleep(18)
		email = bot.find_element_by_id('email')
		password = bot.find_element_by_id('pass')
		#email.clear()
		#password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)

		bot.find_element_by_id('loginbutton').click()

		time.sleep(18)

		#search = bot.find_element_by_class_name("_1frb")
		#search.send_keys(self.query)

	"""def like(self):
					bot = self.bot"""

	def group(self):
		bot = self.bot
		bot.get('https://www.facebook.com/groups/Sri.Lanka.Teachers.Service')
		time.sleep(18)
		#bot.find_element_by_class_name('_2yav').click()
		bot.find_element_by_css_selector("[title^='Files']").click()
		filelist = bot.find_element_by_class_name('_pu_')
		print(filelist)



ed = FbBot('username','password') // replace with login deatils

ed.login()
ed.group()








	