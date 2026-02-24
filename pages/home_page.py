from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.video_instruction = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div.home-card.pointer")
        self.fullscreen_btn = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)")
        self.pause = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__actinview")
        self.fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)")
        self.main_btn = (By.CSS_SELECTOR, "#app > div > div.layout > div > div.material-dialog__window > div > ul > li:nth-child(1)")
        self.group_card = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")
        self.profile_icon = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar")
        self.exit_btn = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(4) > div")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_video_instruction(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video_instruction)).click()

    def click_fullscreen_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_btn)).click()

    def click_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.pause)).click()

    def click_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()

    def click_main_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.main_btn)).click()

    def click_group_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_card)).click()

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_exit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_btn)).click()

    def click_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.confirm_exit)).click()