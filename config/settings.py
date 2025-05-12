class Settings:
    # Browser settings
    CHROME_PROFILE_PATH = 'C:\\Users\\Маргарита\\AppData\\Local\\Google\\Chrome\\User'
    DRIVER_PATH = 'C:\\Users\\Маргарита\\PycharmProjects\\pythonProject5\\auto_practice\\chromedriver.exe'
    SCREENSHOT_DIR = 'C:\\Users\\Маргарита\\PycharmProjects\\pythonProject5\\auto_practice\\data\\'

    # Wildberries URLs
    LOGIN_URL = "https://seller-auth.wildberries.ru/"
    SUPPLIES_URL = "https://seller.wildberries.ru/supplies-management/all-supplies"

    # Booking parameters
    ORDER_NUMBER = '29116625'
    BOOKING_BIDS = [5, 6, 7, 8]
    BEGIN_DAY = 1

    # Timing settings
    MIN_DELAY = 0.1
    MAX_DELAY = 1.1
    PAGE_LOAD_TIMEOUT = 10
