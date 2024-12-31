from selenium import webdriver
import pytest
from pages.demo_test import DemoTest
from pages.buttons import ButtonsPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_search(driver):
        driver.get(ButtonsPage.url) # navigate to the url
        demo_test = DemoTest(driver) # initialize the demo test class
        demo_test.click_search_box() # click the search box
        demo_test.search_for_text("New York") # search for the text
        demo_test.verify_filter("Showing 1 to 5 of 5 entries (filtered from 24 total entries)")
        time.sleep(2)

        assert demo_test.verify_five_entries("New York"), "The office location is not correct"
        assert "Showing 1 to 5 of 5 entries (filtered from 24 total entries)" in driver.page_source, "The search result is not correct"

