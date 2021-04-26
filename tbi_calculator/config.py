""" Parses the configuation file 'config.ini'"""

import configparser
from pathlib import Path

default_config = configparser.ConfigParser()
default_config["Smartsheet"] = {
    "API_KEY": "",
    "SHEET_NAME": "TBI Exclusions",
    "COLUMN_NAME": "Syteline Account Code",
}
default_config["Metabase"] = {"URL": "", "QUERY_NUMBER": "82"}

config = configparser.ConfigParser()
file_path = Path("config.ini")

try:
    config.read(file_path)
except FileNotFoundError:
    with open(file_path, "w") as f:
        default_config.write(f)
    config = default_config
