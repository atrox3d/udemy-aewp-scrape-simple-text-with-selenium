from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver(url):
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    """
    https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
    selenium downloads automatically the driver in ~/.cache/...
    """
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def main():
    driver = get_driver('https://automated.pythonanywhere.com/login/')

    element = driver.find_element(by="id", value='id_username')
    element.send_keys('automated')

    element = driver.find_element(by="id", value='id_password')
    element.send_keys('automatedautomated')
    element.send_keys(Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)

    element = driver.find_element(by='xpath', value='/html/body/nav/div/a')
    element.click()
    time.sleep(2)
    print(driver.current_url)


main()
