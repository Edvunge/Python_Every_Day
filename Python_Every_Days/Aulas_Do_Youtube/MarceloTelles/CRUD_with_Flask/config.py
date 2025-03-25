import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATEBASE_URI = 'mysql+pymysql://root2:usbw@localhost/test'