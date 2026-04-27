import os


class Database:
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')


class Secrets:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')


SENSENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
FROM_EMAIL = os.getenv('FROM_EMAIL')
