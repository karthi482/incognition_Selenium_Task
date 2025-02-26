import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


incogniton_profile_id = '6bfd7e4d-4a2b-4e77-ab1b-930d4090f361'
incogniton_url = f'http://127.0.0.1:35000/automation/launch/python/{incogniton_profile_id}'

# Start the profile
resp = requests.get(incogniton_url)
incomingJson = resp.json()

# Connect Selenium to Incogniton
driver = webdriver.Remote(
    command_executor=incomingJson['url'],
    options=webdriver.ChromeOptions()
)

def wait_and_click(driver, xpath, timeout=30):
    """Wait for an element to be clickable and then click."""
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def wait_and_send_keys(driver, selector, text, timeout=30):
    """Wait for an input field and send keys."""
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).send_keys(text)



# Open the Instantly login page
driver.get('https://app.instantly.ai/app/accounts')

# Wait for the email input field to be present

# Login credentials
email = 'chetan@cleverviral.co'
password = 'LgS_4PnP5BZBg**'

# Enter login credentials
# try:
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))

driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[form="loginForm"]').click()
# except:
#     pass

# Wait for dashboard to load
time.sleep(15)

    # Click "Add new"
list1=['sandra@churneynetwork.pro','sandra@churneyClientHub.pro','sandra@churneyNetworkHub.pro']
for i in list1:
    wait_and_click(driver, '//button[contains(., "Add new")]', timeout=10)
    time.sleep(2)

    # Select "Gmail / G-Suite"
    wait_and_click(driver, "(//h6[text()='Gmail / G-Suite'])[2]", timeout=30)
    time.sleep(2)

    # Click "Yes, IMAP has been enabled"
    wait_and_click(driver, '//button[text()="Yes, IMAP has been enabled"]', timeout=30)
    time.sleep(2)

    # Click "Option 1: oAuth"
    wait_and_click(driver, '//div[h6[text()="Option 1: oAuth"]]', timeout=30)
    time.sleep(3)

    wait_and_click(driver, '//button[h6[text()="Login"]]', timeout=30)
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened window
    time.sleep(5)


    try:
        # wait_and_click(driver, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[3]/div/div/div[2]', timeout=30)
        wait_and_click(driver,
                       '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[4]/div/div/div[2]',
                       timeout=30)
        time.sleep(2)

    except:
        pass

    time.sleep(7)
    gmail=f'{i}'
    gpass='sandra12345@'
    wait_and_send_keys(driver, "input[type='email']", gmail, timeout=50)
    time.sleep(2)
    wait_and_click(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span",
                       timeout=30)
    time.sleep(5)
    wait_and_send_keys(driver, "input[type='password']", gpass, timeout=100)
    time.sleep(5)
        # wait_and_click(driver, "//button[.//span[text()='Next']]", timeout=100)
    wait_and_click(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span",
                       timeout=100)
    time.sleep(6)
    try:
        wait_and_click(driver, "input[value='I understand']", timeout=5)
    except:
        pass
    wait_and_click(driver, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span', timeout=30)
    time.sleep(5)
    # wait_and_click(driver, '//button[span[text()="Allow"]]', timeout=30)
    wait_and_click(driver, '/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div/button/span', timeout=30)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, '//div[@role="status" and @aria-live="polite" and text()="Connected"]')))
    time.sleep(5)
    try:
        wait_and_click(driver, '//span//h6[text()="Back"]')
    except:
        pass







