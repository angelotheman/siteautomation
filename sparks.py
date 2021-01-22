from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.thesparksfoundationsingapore.org/")


#KNOW_MORE
know_more = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/a")
know_more.click()
time.sleep(5)

#Executive Team
try:
	executive_team = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/ul/li[4]/a"))
		)
	
	executive_team.click()

finally:
	#HomePage
	home_page = driver.find_element_by_tag_name("img")
	home_page.click()

#LEARN MORE
driver.implicitly_wait(15)
learn_more_btn = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a")
learn_more_btn.click()

#Fill in the forms
name_column = driver.find_element_by_name("Name")
name_column.send_keys("Angelo")
name_column.send_keys(Keys.TAB)


email_column = driver.find_element_by_name("Email")
email_column.send_keys("ktwum721@gmail.com")

role_selection = Select(driver.find_element_by_tag_name("select"))
role_selection.select_by_index(3)


submit = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]")
submit.click()
time.sleep(10)

#Intern positions
intern_positions = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul/li[5]")
intern_positions.click()
driver.implicitly_wait(10)

#Expert Mentor
expert_mentor = driver.find_element_by_link_text("Expert Mentor")
expert_mentor.click()
driver.implicitly_wait(10)

driver.quit()
