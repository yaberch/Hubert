import os
from dataclasses import dataclass

@dataclass
class Config:
    # Délais et timeouts
    RETRY_COUNT: int = 3
    WAIT_TIMEOUT: int = 15
    MIN_SLEEP: float = 1.0
    MAX_SLEEP: float = 3.0
    
    # Chemins
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    
    # Facebook URLs
    FB_URL = "https://www.facebook.com"
    
    # Credentials
    FB_USERNAME = os.getenv('FB_USERNAME')
    FB_PASSWORD = os.getenv('FB_PASSWORD')
    
    # Mode debug
    DEBUG = os.getenv('DEBUG_MODE', 'False').lower() == 'true'

config = Config()
