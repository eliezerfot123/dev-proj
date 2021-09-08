from .base import *  # noqa
from .base import env
import logging


DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="*")

ADMINS = [
    ('Info', 'eliezerfot123@gmail.com'),
]

MANAGERS = [
    ('Info', 'eliezerfot123@gmail.com'),
]