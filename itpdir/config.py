from ConfigParser import SafeConfigParser
from os.path import abspath, join, normpath

config = SafeConfigParser()
config_path = normpath(join(abspath(__file__), '..', '..', 'itpdir.cfg'))
config.read(config_path)