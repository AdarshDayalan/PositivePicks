from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.ftndaily.com/nba/prizepicks-predictions-tool')

# # Before getting the page, emulate the geolocation
# driver.execute_cdp_cmd("Emulation.setGeolocationOverride", coordinates)

# driver.implicitly_wait(1)
# driver.get("https://app.prizepicks.com/login")

# email_input = driver.find_element(By.ID, 'email-input')
# email_input.clear()
# email_input.send_keys('adarshdayal7@gmail.com')

# password_parent = driver.find_element(By.CLASS_NAME, 'password-input')
# password_input = password_parent.find_element(By.TAG_NAME, 'input')
# password_input.send_keys('Skye123!')

# submit_button = driver.find_element(By.ID, 'submit-btn')
# submit_button.click()