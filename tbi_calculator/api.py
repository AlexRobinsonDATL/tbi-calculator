"""Defines objects that communicate with 3rd party APIs
"""

from typing import Any, Dict, List, Optional

import smartsheet


class Smartsheet(smartsheet.Smartsheet):
    """Extends the smartsheet-sdk object with custom methods"""

    def __init__(self, access_token: Optional[str] = None):
        """Set up base client object

        Parameters
        ----------
        access_token : Optional[str], optional
            Access token for making client requests.
        """
        super().__init__(access_token=access_token)

    def get_column(self, sheet_id: str, column_name: str) -> List[Any]:
        sheet = self.Sheets.get_sheet(sheet_id)
        column_map: Dict[str, int] = {
            column.title: column.id for column in sheet.columns
        }
        column_id = column_map.get(column_name)
        return [row.get_column(column_id).value for row in sheet.rows]
