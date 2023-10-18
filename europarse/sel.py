from selenium import webdriver
import time


def retry_request(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    html_code = driver.page_source

    driver.quit()

    return html_code
