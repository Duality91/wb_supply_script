class Selectors:
    PHONE_INPUT = ('xpath', '//input[@data-testid="phone-input"]')
    SUBMIT_BUTTON = ('xpath', '//button[@data-testid="submit-phone-button"]')
    ORDER_NUMBER = ('xpath', '//span[text()="{}"]')  # Will be formatted
    PLAN_SUPPLY = ('xpath', '//span[text()="Запланировать поставку"]')
    TABLE_BODY = ('xpath', '//tbody')
    CALENDAR_CELLS = ('xpath', '//td//*[contains(@class, "Portal-tooltip")]')
    BOOK_BUTTON = ('xpath', '//button/span[text()="Запланировать"]')
    ACTION_MOVE = ('xpath', '(//td//*[text()="Приёмка"])')
    CHOOSE_BUTTON = ('xpath', '//button/*[text()="Выбрать"]')
