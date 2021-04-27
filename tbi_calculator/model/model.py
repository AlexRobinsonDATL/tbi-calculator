""" An object that controls and stores data used in the app"""

from configparser import ConfigParser

from metabase import Metabase
from simple_smartsheet import Smartsheet
from simple_smartsheet.exceptions import SmartsheetError

from ..config import config
from .base import Model
from .datastructures import TBITable


class SSMetabaseModel(Model):
    """Model using Smartsheet for the exclusion_list and getting sales date from Metabase"""

    def __init__(self, config: ConfigParser = config):
        self.config = config

    def fetch_data(  # type: ignore
        self, metabase_email: str, metabase_password: str
    ) -> None:
        self._fetch_exclusion_list()
        self._fetch_tbi_data(metabase_email, metabase_password)

    def _fetch_exclusion_list(self) -> None:
        api_key = self.config["Smartsheet"]["api_key"]
        sheet_name = self.config["Smartsheet"]["sheet_name"]
        column_name = self.config["Smartsheet"]["column_name"]

        try:
            smartsheet = Smartsheet(api_key)
            sheet = smartsheet.sheets.get(sheet_name)
        except SmartsheetError:
            raise ValueError("Could not download smartsheet")

        self.exclusion_list = list(
            {
                row[column_name]
                for row in sheet.as_list()
                if row[column_name] is not None
            }
        )

    def _fetch_tbi_data(self, metabase_email: str, metabase_password: str) -> None:
        metabase = Metabase(
            email=metabase_email,
            password=metabase_password,
            endpoint=self.config["Metabase"]["url"],
        )
        card_number = self.config["Metabase"]["query_number"]
        tbi_data = metabase.post(f"/card/{card_number}/query")
        self.table = TBITable(tbi_data)

    def filter(self) -> None:
        self.table.remove_dunlop()
        self.table.exclude(self.exclusion_list)

    def total_sales(self, tyre_type: str) -> float:
        return self.table.total_sales(tyre_type)
