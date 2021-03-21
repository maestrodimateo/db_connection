import pymysql
import yaml
pymysql.install_as_MySQLdb()


# Parsing yaml format into python list
def parse_yaml_data():
    config_file = open('config.yaml')
    return yaml.load(config_file, Loader=yaml.FullLoader)


conf = parse_yaml_data()

# connection for mysql
db_connection = "{0}://{1}:{2}@{3}/{4}".format(
    conf['db_connector'],
    conf['db_user'],
    conf['db_password'],
    conf['db_host'],
    conf['db_name']
)

# connection for mongodb
mongo_connection = '{0}://{1}:{2}@{3}/{4}?retryWrites=true&w=majority'.format(
    conf['mongo_host'],
    conf['mongo_user'],
    conf['mongo_password'],
    conf['mongo_cluster'],
    conf['mongo_name']
)
