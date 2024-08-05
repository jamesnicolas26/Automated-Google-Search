from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def automate_google_search(query):
    """Automate a Google search using Selenium."""
    try:
        # Set up the web driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Open Google
        driver.get("https://www.google.com")

        # Find the search box and enter the query
        search_box = driver.find_element("name", "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(3)

        # Print the titles of the first few search results
        results = driver.find_elements("css selector", "h3")
        for i, result in enumerate(results[:5], start=1):
            print(f"{i}. {result.text}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


def main():
    query = input("Enter your search query: ")
    automate_google_search(query)


if __name__ == "__main__":
    main()
