from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *
import undetected_chromedriver as uc
import pyautogui
from bs4 import BeautifulSoup
import pandas as pd

options = uc.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.headless = False
options.add_argument("--disable-extensions")
options.add_argument("--window-size=1920,1080")
options.add_argument('--log-level=1')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-notifications")

#import line of code 
#DO NOT DELETE (don't know how it started working)
options.add_argument("--user-data-dir=C:/Users/adars/AppData/Local/Google/Chrome/User Data/Profile 7")


# Pass the argument 1 to allow and 2 to block
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)

driver = uc.Chrome(
    options=options,
    browser_executable_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
)
driver.get("https://app.prizepicks.com/")


wait = WebDriverWait(driver, 5)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
driver.find_element(By.XPATH, "//div[@class='name'][normalize-space()='NBA']").click()

time.sleep(2)
print(driver.find_element(By.XPATH, "//div[@class='name'][normalize-space()='NBA']").text)

# Makes sure the stat_container element is available before attempting to access it
stat_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "stat-container")))


# Parse the HTML using BeautifulSoup


# Find the div with class 'pp-container' and extract the stat names
soup = BeautifulSoup(driver.page_source, "html.parser")
stat_container = soup.find('div', class_='pp-container stat-container')
stat_names = [stat.text.strip() for stat in stat_container.find_all('div', class_='stat')]

# Print the extracted stat names
print(stat_names)

# Creates the list where the props will be stored
result = []

for stats in stat_names:
    driver.find_element(By.XPATH, f"//div[text()='{stats}']").click()
    print(driver.find_element(By.XPATH, f"//div[text()='{stats}']").text)
    projections = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "projections-list")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    projections_list = soup.find('ul', class_='projections-list')
    for projection in projections_list.find_all('li', class_='projection'):
        name = projection.find('h3', class_='name').text.strip()
        game_time = projection.find('time', class_='date').text.strip()
        opp = projection.find('p', class_='opponent').text.strip()
        button = projection.find('button', {'aria-label': 'Open modal for Demons and Goblins'})
        if button:
            # Extract alt attribute to determine category
            alt_attribute = button.find('img')['alt']
            
            if alt_attribute == 'Demon':
                category = 'Demon'
            elif alt_attribute == 'Goblin':
                category = 'Goblin'
            else:
                category = 'Regular'
            
            # Handle projections with the attribute
            line = projection.find('div', class_='presale-score').text.strip()
        else:
            # Handle projections without the attribute
            line = projection.find('div', class_='score').text.strip()
            line = line.split(".")[0] + '.' + line.split(".")[1][:1]
            category = 'Regular'

        result.append({'Name': name, 'Game Time': game_time, 'Opponent': opp,'Category': stats, 'Line': line, 'Line_Type': category})
        print(f"Name: {name}, Game Time: {game_time}, Opponent: {opp}, Category: {stats}, statsLine: {line}, Line_Type: {category}")

df = pd.DataFrame(result)