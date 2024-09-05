from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from secretenv import USERNAME, PASSWORD

def scroll_down(browser):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        sleep(10)

        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height

def login():
    # begin script
    browser = webdriver.Firefox()
    browser.get("http://www.facebook.com")

    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    submit = browser.find_element_by_id("u_0_b")  # is this static?
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    submit.click()
    return browser
