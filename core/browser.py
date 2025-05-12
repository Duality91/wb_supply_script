from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.settings import Settings


class BrowserManager:
    def __init__(self):
        self.settings = Settings()
        self.driver = None
        self._setup_options()

    def _setup_options(self):
        self.options = Options()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-notifications")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument(f"--user-data-dir={self.settings.CHROME_PROFILE_PATH}")

    def start_browser(self):
        self.service = Service(self.settings.DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.maximize_window()
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
