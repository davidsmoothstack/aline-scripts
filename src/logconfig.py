import logging
import sys


logging_format = "[%(asctime)s] %(message)s"
logging_date_format = "%b %d %Y %X"

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    datefmt=logging_date_format,
    handlers=[
        logging.FileHandler("logs.txt"),
        logging.StreamHandler(sys.stdout)
    ]
)
