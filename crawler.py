import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Set up the Selenium WebDriver with a random User-Agent
options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua.random
print(user_agent)
options.add_argument(f'--user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

# Waiting for page to load, adjust as needed
url = 'https://www.google.com'
driver.get(url)

# Define variables
all_html_content = ''
unique_usernames = set()
save_interval = 5  # Save Excel file every 5 scrolls
total_scrolls = 8000  # Total number of scrolls
time.sleep(60)  # Add a break in time to be able to enter the search prompt

# Perform a series of key presses to scroll down
actions = ActionChains(driver)
for i in range(total_scrolls):
    time.sleep(5)  # Adjust the sleep time as needed
    page_source = driver.page_source  # Get the HTML code from the page
    all_html_content += page_source  # Compile it to a variable
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
   
    # Extract and store unique usernames every save_interval scrolls
    if i % save_interval == 0 and i != 0:
        soup = BeautifulSoup(all_html_content, 'html.parser')
        
        # Extract usernames from <a> tags
        user_elements = soup.find_all('a')
        unique_usernames.update(element.get_text() for element in user_elements if element.get('href', '').startswith('https://onlyfans.com/'))
        
        # Extract usernames using regex from HTML content
        user_text = soup.get_text()
        user = re.findall(r'@\w+', user_text)
        unique_usernames.update(user)

        # Update the Excel file with new usernames
        try:
            df_temp = pd.read_excel('only_file_final.xlsx')
        except FileNotFoundError:
            df_temp = pd.DataFrame(columns=['Link'])

        df_new = pd.DataFrame(list(unique_usernames), columns=['Link'])

        # Concatenate the existing DataFrame with the new usernames DataFrame
        df_updated = pd.concat([df_temp, df_new], ignore_index=True)

        # Keep the last occurrence of each link to maintain corresponding Account_Name
        df_updated = df_updated.drop_duplicates(subset='Link', keep='last')

        # Update the Account_Name column using the Link column
        df_updated['Account_Name'] = df_updated['Link'].str.replace('https://onlyfans.com/', '@')

        # Save the updated DataFrame to the Excel file
        df_updated.to_excel('only_file_final.xlsx', index=False)

        # Reset for the next batch
        all_html_content = ''
        unique_usernames = set()

# Close the browser window
driver.quit()
