from selenium import webdriver
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


def clean_text(text):
    """extract only the temp from the text"""
    _, temp = text.split(': ')
    return float(temp)


def main():
    driver = get_driver('http://automated.pythonanywhere.com')
    xpath = '/html/body/div[1]/div/h1[1]'
    xpath = '/html/body/div[1]/div/h1[2]'
    time.sleep(2)
    element = driver.find_element(
                        by="xpath",
                        value=xpath
    )
    return clean_text(element.text)


print(main())
