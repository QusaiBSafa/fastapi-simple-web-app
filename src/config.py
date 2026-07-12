import os

class Config:
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'FastAPI Simple Web App')
    VERSION = os.getenv('VERSION', '1.0')
    DEBUG = os.getenv('DEBUG', 'true').lower() in ['true', '1', 't']