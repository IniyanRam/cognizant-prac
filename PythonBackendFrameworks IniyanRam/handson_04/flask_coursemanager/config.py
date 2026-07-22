import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///coursemanager.db'
    SECRET_KEY = 'supersecretkey'
    DEBUG = True
