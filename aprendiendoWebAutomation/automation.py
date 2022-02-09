# # automatizacion para internet
# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com/')

# # search_box = driver.find_element_by_name('search_query')
# search_box = driver.find_elements_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
# search_box.send_keys('Barbakahn')
# time.sleep(5)
# search_box.submit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/watch?v=nXbfZL5kttM")

WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-label='Play']"))).click()
