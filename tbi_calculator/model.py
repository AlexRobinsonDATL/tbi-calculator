import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

import smartsheet

logger = logging.getLogger(__name__)


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


@dataclass
class TBIRow:
    customer_order: str
    line_release: str
    customer: str
    customer_name: str
    item: str
    description: Optional[str]
    qty_ordered: int
    to_credit: int
    to_invoice: int
    qty_shipped: int
    qty_invoiced: int
    amount: float
    um: str
    tci: str
    release_note: str
    release_date: datetime
    sales_person: str
    currency_code: str
    converted_amount: float

    @property
    def order_type(self) -> str:
        if self.customer_order.startswith("N"):
            return "New"
        elif self.customer_order.startswith("R"):
            return "Retread"
        else:
            return "Not Specified"

    def is_dunlop(self) -> bool:
        return (
            "DUNLOP" in self.customer_name
            or "D085" in self.customer
            or "D086" in self.customer
        )


class TBITable:
    rows: List[TBIRow]

    def __init__(self, metabase_reponse: Dict):
        self.rows = self._parse_response(metabase_reponse)

    @staticmethod
    def _parse_response(metabase_reponse) -> List[TBIRow]:
        rows = metabase_reponse[1]["data"]["rows"]
        return [TBIRow(*row) for row in rows]
