""" Parses the configuation file 'config.ini'"""

import configparser
from pathlib import Path

default_config = configparser.ConfigParser()

default_config["Smartsheet"] = {
    "API_KEY": "",
    "SHEET_ID": "8604312818476932",
    "COLUMN_NAME": "Syteline Account Code",
}

default_config["Metabase"] = {"URL": "", "QUERY_NUMBER": "82"}


config = configparser.ConfigParser()

file_path = Path(__file__).parents[1] / "config.ini"

try:
    with open(file_path, "r") as f:
        config.read(f)
except FileNotFoundError:
    with open(file_path, "w") as f:
        default_config.write(f)
