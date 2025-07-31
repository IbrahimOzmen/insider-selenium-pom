# utils/logger_config.py
import logging
import os
from datetime import datetime
from config.config import Config

# Create logs directory if it doesnt exist
log_dir = os.path.join(Config.BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)

# Create log filename with current date
log_filename = f"insider_automation_{datetime.now().strftime('%Y%m%d')}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Define logging format for consistent output
formatter = logging.Formatter(
    fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create main logger instance
logger = logging.getLogger("insider_logger")
# Set logging level to DEBUG for comprehensive logging
logger.setLevel(logging.DEBUG)  # Available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(log_filepath, encoding="utf-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Add handlers only if not already added to prevent duplicate logs
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
