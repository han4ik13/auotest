from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/')

    def click_nokia(self):
        nokia = self.browser.find_element(By.XPATH, '//a[text()="Nokia lumia 1520"]')
        nokia.click()

    def click_monitors(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_monitors_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
