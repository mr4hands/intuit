import configparser

def get_config(file):
    configfile = configparser.ConfigParser()
    configfile.read(file)
    return configfile


config = get_config('configmodule/config.ini')
