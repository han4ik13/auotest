import time
from pages.homepage import HomePage
from pages.productpage import ProductPage


def test_open_nokia(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_nokia()
    productpage = ProductPage(browser)
    productpage.check_title_is("Nokia lumia 1520")


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitors()
    time.sleep(5)
    homepage.check_monitors_count(2)
