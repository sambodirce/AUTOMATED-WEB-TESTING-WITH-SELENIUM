from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_app():
    # Initialize Firefox WebDriver with the specified Firefox binary path and GeckoDriver executable path
    driver = webdriver.Firefox(firefox_binary='/usr/bin/firefox', executable_path='/home/sambd001/Documents/selenium/geckodriver')

    # Open a website
    driver.get('https://example.com')

    # Find an element by its XPath and assert its text
    element = driver.find_element(By.XPATH, '//h1')
    assert element.text == 'Example Domain'

    # Close the browser
    driver.quit()

# Call the test function
test_web_app()
