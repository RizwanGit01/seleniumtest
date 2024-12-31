from selenium.webdriver.common.by import By


class ButtonsPage:
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    search_box = (By.XPATH, "//input[@type='search']")
    verify_search_result = (By.XPATH, "//div[@id='example_info']")
    table = (By.XPATH, "//table[@id='example']/tbody/tr")
    table_row = (By.XPATH, ".//td[3]")
