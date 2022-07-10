"""
Probs just run some shit code here tbh...
"""
import time
import random
import json

from playwright.sync_api import sync_playwright
from typing import Optional
from string_cleaning import clean_str
from data_saver import DataSaver, JSONSaver


class RequestChecker:

    def __init__(self, url: str, driver, data_saver: DataSaver):
        self.url = url
        self.driver = driver
        self.data_saver = data_saver(folder_name='responses', filename=clean_str(self.url))
        self.responses = {}  # to store responses

    def get_page_responses(self, headless: bool = False, pause: float = 3):
        browser = self.driver.chromium.launch(headless=headless)
        page = browser.new_page()

        page.on("response", lambda response: self.update_responses(response))
        page.goto(self.url, timeout=0)

        time.sleep(pause)  # wait whilst we load

        browser.close()

    def update_responses(self, response):
        try:
            self.responses[response.url] = response.json()
        except:
            self.responses[response.url] = {"error": "empty or invalid request",
                                            "response_body": str(response.body())}

    def save_results(self):
        self.data_saver.save_data(self.responses)


if __name__ == '__main__':
    with sync_playwright() as p:
        test = RequestChecker(url='http://quotes.toscrape.com/scroll', driver=p, data_saver=JSONSaver)
        test.get_page_responses(headless=False)
        test.save_results()
