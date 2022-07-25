# -*- encoding: utf-8 -*-

import os
import configparser


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Connection to .config
    config = configparser.RawConfigParser()
    config.read('.config')
    conf = dict(config.items('db_config'))

    # Set up the App SECRET_KEY
    SECRET_KEY = conf['secret_key']

    # This will create a file in <app> FOLDER

    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(conf['db_engine'], conf['db_username'],
                                                                 conf['db_pass'], conf['db_host'],
                                                                 conf['db_port'], conf['db_name'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # MYSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE', 'mysql'),
        os.getenv('DB_USERNAME', 'adminlte'),
        os.getenv('DB_PASS', 'server10pass'),
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_PORT', 3306),
        os.getenv('DB_NAME', 'adminlte')
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
