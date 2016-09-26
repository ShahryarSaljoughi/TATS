__author__ = 'shahryar_slg'

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' +\
                          os.path.join('', BASE_DIR + '\\database\\info.db')


