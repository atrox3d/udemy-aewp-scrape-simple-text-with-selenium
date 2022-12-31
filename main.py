from selenium import webdriver


def get_driver(url):
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def main():
    driver = get_driver('http://automated.pythonanywhere.com')
    element = driver.find_element(by="xpath",
                                  value='/html/body/div[1]/div/h1[1]')
    return element.text


print(main())
