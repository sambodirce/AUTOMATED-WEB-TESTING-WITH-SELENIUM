from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def test_web_app():
    # Initialize Firefox WebDriver with Firefox options
    options = Options()
    options.binary_location = '/usr/bin/firefox'  # Specify the path to the Firefox binary
    driver = webdriver.Firefox(options=options)

    # Open a website
    driver.get('https://example.com')
    # Find an element by its XPath and assert its text
    element = driver.find_element(By.XPATH, '//h1')
    assert element.text == 'Example Domain'
    # Close the browser
    driver.quit()

# Call the test function
test_web_app()


