import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.lessons_page import LessonsPage
from pages.homework_page import HomeworkPage


# ================== VALID LOGIN ==================

def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("Kammy_2112")
    time.sleep(2)
    auth_page.click_btn_password()

    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except NoSuchElementException:
        pass

    home_page = HomePage(driver_chrome)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_fullscreen_btn()
    time.sleep(5)
    home_page.click_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit()
    time.sleep(2)
    home_page.click_main.btn()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)
    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_exit_btn()
    time.sleep(2)
    home_page.click_confirm_exit()

    lesson_page = LessonsPage(driver_chrome)
    lesson_page.click_lessons_btn()
    time.sleep(2)
    lesson_page.click_last_lesson()
    time.sleep(2)
    lesson_page.click_fullscreen_btn()
    time.sleep(2)
    lesson_page.click_play_btn()
    time.sleep(10)
    lesson_page.click_fullscreen_exit()
    time.sleep(2)
    lesson_page.click_main_btn()
    time.sleep(2)

    homework_page.open_homeworks_btn()
    time.sleep(2)
    homework_page.open_homework_autotesting()
    time.sleep(2)
    homework_page.click_task_btn()
    homework_page.write_comment("Test Comment")
    homework_page.click_send_btn()
    time.sleep(2)


def test_auth_firefox(driver_firefox):
    driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_firefox)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("Kammy_2112")
    time.sleep(2)
    auth_page.click_btn_password()
    time.sleep(2)

    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except NoSuchElementException:
        pass

    home_page = HomePage(driver_firefox)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_fullscreen_btn()
    time.sleep(5)
    home_page.click_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit()
    time.sleep(2)


def test_auth_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_edge)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("Kammy_2112")
    time.sleep(2)
    auth_page.click_btn_password()

    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except NoSuchElementException:
        pass


# ================== INVALID LOGIN ==================

def test_invalid_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("wrong_password")
    time.sleep(2)
    auth_page.click_btn_password()


def test_invalid_auth_firefox(driver_firefox):
    driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_firefox)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("wrong_password")
    time.sleep(2)
    auth_page.click_btn_password()


def test_invalid_auth_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_edge)

    auth_page.enter_login("998990338063")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("wrong_password")
    time.sleep(2)
    auth_page.click_btn_password()
