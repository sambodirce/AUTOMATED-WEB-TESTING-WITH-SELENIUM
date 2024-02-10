from selenium import webdriver

def test_web_app():
    # Initialize WebDriver (replace 'chromedriver' with the path to your driver executable)
    driver = webdriver.Chrome('/home/sambd001/Documents/selenium/chromedriver')

    # Open a website
    driver.get('https://example.com')

    # Find an element by its ID and click it
    element = driver.find_element_by_id('some_id')
    element.click()

    # Close the browser
    driver.quit()

# Call the test function
test_web_app()
