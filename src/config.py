from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
SECRET_KEY = os.environ.get('SECRET_KEY')
MANAGER_SECRET_KEY = os.environ.get('MANAGER_SECRET_KEY')



