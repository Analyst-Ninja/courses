import logging
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('file.log',maxBytes=2000,backupCount=5)

# possible values of when
# s, m, h, d, midnight, w0--> monday, w1--> tuesday
handler = TimedRotatingFileHandler("Timefile.log", when="s", interval=1, backupCount=5)

logger.addHandler(handler)
for _ in range(6):
    logger.info("This is a info")
    time.sleep(5)
