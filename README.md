# QA Selenium Test by Rizwan Shaik

## Objective
Automate the validation of search functionality on the Selenium Playground website.

## Setup Instructions

1. **Install Dependencies**:
   - Ensure you have Python and pip installed.
   - Install Selenium: `pip install selenium`
   - Install pytest: `pip install pytest`

2. **WebDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and ensure it's in your PATH.

3. **Run the Test**:
   - Execute the test using pytest: `pytest qa_selenium_test.py`
   - The browser will open and perform automated actions to validate the search functionality.
   - Run in two major browsers: Chrome and Firefox.

# Page Object Model
- Implemented a Page Object Model for the Selenium Playground Table Search Demo.
- Test cases are organized in a separate file.
- Buttons and input fields are defined as separate objects in `pages/buttons.py`.
- Test case functions are located in `pages/demo_test.py`.
- Test steps are invoked from the test case functions in `pages/demo_test.py`.
- Tests are executed using `pytest`.
- Test steps are invoked in `tests/qa_selenium_test.py`.

## Approach
- The script navigates to the Selenium Playground Table Search Demo.
- It searches for "New York" and validates the search results.
- It verifies the number of entries is 5 for new york.
- Added assertions for the search results and the number of entries.
- Added assertion for number of entries text after search.
- Uses `pytest` for test structure and assertions.
