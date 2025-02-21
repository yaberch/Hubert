import logging
import os
from logging.handlers import RotatingFileHandler
from utils.config import config

def setup_logger(name: str = 'Hubert') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if config.DEBUG else logging.INFO)

    # Créer le dossier de logs s'il n'existe pas
    os.makedirs(config.LOG_DIR, exist_ok=True)

    # Handler pour fichier
    file_handler = RotatingFileHandler(
        os.path.join(config.LOG_DIR, 'hubert.log'),
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))

    # Handler pour console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
