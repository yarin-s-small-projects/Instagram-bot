import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
INSTAGRAM_URL = os.getenv("URL")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)
    
    def login(self):
        self.driver.get(INSTAGRAM_URL)
        # Wait for login page to appear        
        time.sleep(2)
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME,"username")))
        username_input.send_keys(EMAIL)
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME,"password")))
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        
    def find_followers(self):
        # Wait for the main page to apear
        time.sleep(5)
        # Handle pop up if exist
        try:
            popup_btn = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(), 'Not now')]")))
            popup_btn.click()
        except NoSuchElementException:
            pass
        
        print("searching for search button")
        search_btn = self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Search')]")))
        print("Found search button")
        search_btn.click()
        print("Clicked search button")
        
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[aria-label='Search input']")))
        search_input.send_keys(SIMILAR_ACCOUNT)
        print("Entered similar account name")
        
        #Pick the first one
        first_result = self.wait.until(EC.presence_of_element_located((By.XPATH , f"//span[contains(text(), '{SIMILAR_ACCOUNT}')]")))
        first_result.click()
        print("Clicked on similar account")
        
        time.sleep(2)

        similar_accounts_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , "svg[aria-label='Similar accounts']")))
        similar_accounts_btn.click()
        print("Clicked on similar accounts button")
        
        see_all_btn = self.wait.until(EC.presence_of_element_located((By.XPATH , "//span[contains(text(), 'See all')]")))
        see_all_btn.click()
        print("Clicked on see all button")
        
    def follow(self):
        # Wait for followers modal to appear
        time.sleep(2)
        
        # Scroll the followers dialog to load more users
        dialog = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        
        # Find only "Follow" buttons
        follow_buttons = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Follow') and not(contains(text(), 'Following'))]")
        
        print(f"Found {len(follow_buttons)} users to follow")

        for i, button in enumerate(follow_buttons[:10]):  # Limit to first 10 to avoid rate limiting
            try:
                # Scroll button into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(1)
                
                # Try to click
                button.click()
                print(f"Followed user {i+1}")
                time.sleep(2)
                
            except ElementClickInterceptedException:
                print(f"Click intercepted for user {i+1}, trying JavaScript click")
                try:
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(2)
                except Exception as e:
                    print(f"Failed to follow user {i+1}: {e}")
                    continue
            except Exception as e:
                print(f"Error following user {i+1}: {e}")
                continue
        
        print("Finished following users") 
    
    def close_browser(self):
        self.driver.quit()
        
if __name__ == "__main__":
    bot = InstagramBot()
    bot.login()
    bot.find_followers()
    bot.follow()
    bot.close_browser()
        