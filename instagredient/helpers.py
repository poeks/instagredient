import ConfigParser, requests
from flask import redirect


def read_config(config_file="./config.cfg"):
    config = ConfigParser.ConfigParser()
    config.read(config_file)

    return config
