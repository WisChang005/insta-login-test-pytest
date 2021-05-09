import time

import pytest
from selenium.webdriver.common.by import By

from src.drivers import driver_helper
from src.utils.config import InstagramConfig


@pytest.fixture
def chrome_driver():
    yield driver_helper.get_chrome_driver()


def test_instagram_title_is_correct(chrome_driver):
    with chrome_driver as driver:
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")
        assert driver.title == "Instagram"


def test_instagram_login_success(chrome_driver):
    with chrome_driver as driver:
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")

        # input account/pwd
        driver.find_element(By.NAME, "username").send_keys(InstagramConfig.get_instagram_account())
        driver.find_element(By.NAME, "password").send_keys(InstagramConfig.get_instagram_password())

        # click login button
        LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
        driver.find_element(*LOGIN_BUTTON).click()

        # verify loging success
        SEARCH_BAR = (By.XPATH, "//div[@class=\"pbgfb Di7vw \" and @role=\"button\"]")
        assert driver.find_element(*SEARCH_BAR)


def test_instagram_login_fail(chrome_driver):
    with chrome_driver as driver:
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")

        # input account/pwd
        driver.find_element(By.NAME, "username").send_keys("my_account@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("password")

        # click login button
        LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
        driver.find_element(*LOGIN_BUTTON).click()

        # alert verify
        LOGIN_ERROR_ALERT = (By.ID, "slfErrorAlert")
        alert_text = driver.find_element(*LOGIN_ERROR_ALERT).text
        WRONG_PASSWORD_ALERT_TEXT = "Sorry, your password was incorrect. Please double-check your password."
        assert alert_text == WRONG_PASSWORD_ALERT_TEXT
