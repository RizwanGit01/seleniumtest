from pages.buttons import ButtonsPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DemoTest:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_search_box(self,):
        self.driver.find_element(*ButtonsPage.search_box).click()

    def search_for_text(self, text: str):
        search_box = self.driver.find_element(*ButtonsPage.search_box)
        search_box.clear()
        search_box.send_keys(text)

    def verify_filter(self, expected_text: str):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((ButtonsPage.verify_search_result), expected_text))

    def verify_five_entries(self, expected_text: str): # verify the number of entries is 5
        count = 0
        rows = self.driver.find_elements(*ButtonsPage.table) # get the number of rows
        for row in rows:
            office_column = row.find_element(*ButtonsPage.table_row) # get the office column
            print(f"Checking office location: {office_column.text.strip()}") # print the office location for debugging purposes
            if office_column.text.strip().lower() == expected_text.lower(): # check if the office location is correct
                count += 1 # increment the count
        print(f"Count: '{expected_text}' : {count}") # print the count for debugging purposes
        return count == 5 # return True if the count is 5, False otherwise