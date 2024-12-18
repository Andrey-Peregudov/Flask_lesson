import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # POSTS_PER_PAGE = 30
    # SECRET_KEY = 'jjjjjjj'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(basedir, 'python424.db')

