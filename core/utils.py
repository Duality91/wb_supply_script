import logging
from datetime import datetime


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('wildberries_bot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = datetime.now()

    def elapsed(self):
        return (datetime.now() - self.start_time).total_seconds()
