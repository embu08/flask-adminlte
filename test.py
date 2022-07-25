import configparser

config = configparser.RawConfigParser()
config.read('.config')
conf = dict(config.items('db_config'))

SECRET_KEY = conf['secret_key']
SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(conf['db_engine'], conf['db_username'],
                                                             conf['db_pass'], conf['db_host'],
                                                             conf['db_port'], conf['db_name'])
print(SECRET_KEY)
print(SQLALCHEMY_DATABASE_URI)
