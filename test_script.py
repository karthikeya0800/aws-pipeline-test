from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

def test_google_title():
    # Configure Firefox options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (remove for visible mode)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Set up WebDriver service with GeckoDriverManager
    service = Service(GeckoDriverManager().install())

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=service, options=options)
    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for the page to load
        time.sleep(2)

        # Validate title
        expected_title = "Google"
        actual_title = driver.title
        assert expected_title == actual_title, f"Expected '{expected_title}', but got '{actual_title}'"

        print("Test passed: Title is correct.")
    except AssertionError as e:
        print(f"Test failed: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_title()
