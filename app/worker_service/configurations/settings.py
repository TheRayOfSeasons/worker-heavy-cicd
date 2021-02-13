import os

from pathlib import Path

from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

project_folder = os.path.expanduser(BASE_DIR)
load_dotenv(os.path.join(project_folder, '.env'))

INSTALLED_APPS = [
    'ice_creams'
]

BROKER_URL = 'redis://localhost:6379/0'


DATABASE = {
    'ENGINE': os.getenv('DATABASE_ENGINE', 'psycopg2'),
    'NAME': os.getenv('DATABASE_NAME'),
    'USER': os.getenv('DATABASE_USER'),
    'PASSWORD': os.getenv('DATABASE_P>TASSWORD'),
    'HOST': os.getenv('DATABASE_HOST'),
    'PORT': os.getenv('DATABASE_PORT'),
}
