from core.browser import BrowserManager
from core.actions import WildberriesActions
from core.utils import setup_logging, Timer
from config.settings import Settings
from config.selectors import Selectors

logger = setup_logging()


def main():
    timer = Timer()
    timer.start()

    try:
        logger.info("Starting Wildberries Supply Booking Bot")

        # Initialize browser
        browser = BrowserManager()
        driver = browser.start_browser()
        actions = WildberriesActions(driver)
        settings = Settings()
        selectors = Selectors()

        # Format selectors with dynamic values
        order_selector = (selectors.ORDER_NUMBER[0],
                          selectors.ORDER_NUMBER[1].format(settings.ORDER_NUMBER))

        state = True
        while state:
            try:
                driver.get(settings.SUPPLIES_URL)
                actions.random_delay()

                # Find and click order
                actions.wait_and_click(order_selector)

                # Plan supply
                actions.wait_and_click(selectors.PLAN_SUPPLY)

                # Zoom out to see full table
                actions.zoom_page('-')

                # Find available slots
                cells = driver.find_elements(*selectors.CALENDAR_CELLS)
                elements_to_action = driver.find_elements(*selectors.ACTION_MOVE)

                for i in range(settings.BEGIN_DAY, len(cells)):
                    bid_text = cells[i].text.replace("✕", "")

                    if int(bid_text) in settings.BOOKING_BIDS:
                        # Hover and select time slot
                        actions.actions.move_to_element(elements_to_action[i]).perform()
                        actions.random_delay()

                        # Click choose and book
                        actions.wait_and_click(selectors.CHOOSE_BUTTON)
                        actions.wait_and_click(selectors.BOOK_BUTTON)

                        logger.info(f"Successfully booked slot with bid: {bid_text}")
                        actions.take_screenshot()
                        state = False
                        break

                # Zoom back in
                actions.zoom_page('+')
                actions.random_delay()

            except UnexpectedAlertPresentException:
                actions.handle_alerts()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        browser.close_browser()
        logger.info(f"Script completed in {timer.elapsed():.2f} seconds")


if __name__ == "__main__":
    main()
