import os
import logging
from from_root import from_root
from datetime import datetime


LOG_FILE=f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
log_path=os.path.join(from_root(),"logs",LOG_FILE)

os.makedirs(os.path.dirname(log_path), exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

file_handler=logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
