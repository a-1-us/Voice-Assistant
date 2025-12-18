from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def search_wikipedia(query):
    # Initialize the Chrome WebDriver with specific path
    service = Service("C:\\Users\\tanus\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to Wikipedia
        driver.get("https://www.wikipedia.org")

        # Find and interact with the search box
        search_box = driver.find_element(By.ID, "searchInput")
        search_box.send_keys(query)
        
        # Find and click the search button
        search_button = driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive")
        search_button.click()

        # Wait a bit to see the results
        time.sleep(60)
    finally:
        # Close the browser
        driver.quit()


