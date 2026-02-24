from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomeworkPage():
    def __init__(self, driver):
        self.driver = driver
        self.homeworks_btn = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(4)")
        self.homework_autotesting = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(2) > div.work-dropdown.homework-card_drop.grow > div > div")
        self.task_btn = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(2) > div.work-dropdown.homework-card_drop.grow.homework-card_drop-active > div.work-dropdown-content > div > button")
        self.comment_input = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea")
        self.send_btn = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button")

    def open_homeworks_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homeworks_btn)).click()

    def open_homework_autotesting(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homework_autotesting)).click()

    def click_task_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.task_btn)).click()

    def write_comment(self, comment_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.comment_input)).send_keys(comment_input)

    def click_send_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.send_btn)).click()
