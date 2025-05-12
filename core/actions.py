import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (UnexpectedAlertPresentException,
                                        NoAlertPresentException)
from config.settings import Settings
from config.selectors import Selectors


class WildberriesActions:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.settings = Settings()
        self.selectors = Selectors()
        pyautogui.FAILSAFE = False

    def zoom_page(self, mode: str, zoom_times: int = 4):
        """Zoom page in/out using keyboard shortcuts"""
        pyautogui.keyDown('ctrl')
        for _ in range(1, zoom_times + 1):
            pyautogui.press(f'{mode}')
        pyautogui.keyUp('ctrl')

    def handle_alerts(self):
        """Handle unexpected alerts"""
        try:
            time.sleep(random.uniform(0.2, 1.1))
            alert = self.driver.switch_to.alert
            time.sleep(random.uniform(0.1, 1.1))
            alert.accept()
            time.sleep(random.uniform(0.2, 1.0))
        except NoAlertPresentException:
            pass

    def random_delay(self):
        """Random delay between actions"""
        time.sleep(random.uniform(self.settings.MIN_DELAY, self.settings.MAX_DELAY))

    def wait_and_click(self, selector):
        """Wait for element and click it"""
        element = WebDriverWait(self.driver, self.settings.PAGE_LOAD_TIMEOUT).until(
            EC.element_to_be_clickable(selector)
        )
        element.click()
        self.random_delay()

    def take_screenshot(self):
        """Take screenshot with timestamp"""
        timestamp = str(time.time())
        self.driver.save_screenshot(
            f"{self.settings.SCREENSHOT_DIR}{timestamp}.png"
        )

