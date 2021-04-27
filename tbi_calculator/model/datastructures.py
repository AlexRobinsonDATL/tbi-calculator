"""Defines data structures for use in models
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class TBIRow:
    customer_order: str
    line_release: str
    customer_code: str
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

    def _customer_name_is_dunlop(self) -> bool:
        if self.customer_name is None:
            return False
        return "DUNLOP" in self.customer_name

    def _customer_code_is_dunlop(self) -> bool:
        if self.customer_code is None:
            return False
        return self.customer_code.startswith("D085") or self.customer_code.startswith(
            "D086"
        )

    def is_dunlop(self) -> bool:
        return self._customer_code_is_dunlop() or self._customer_name_is_dunlop()


class TBITable:
    rows: List[TBIRow]

    def __init__(self, metabase_reponse: Dict):
        self.rows = self._parse_response(metabase_reponse)

    @staticmethod
    def _parse_response(metabase_reponse) -> List[TBIRow]:
        rows = metabase_reponse[1]["data"]["rows"]
        return [TBIRow(*row) for row in rows]

    def remove_dunlop(self) -> None:
        self.rows = [row for row in self.rows if not row.is_dunlop()]

    def exclude(self, exclusion_list: List[str]) -> None:
        self.rows = [
            row for row in self.rows if row.customer_code not in exclusion_list
        ]

    @property
    def customer_codes(self) -> Set[str]:
        return {row.customer_code for row in self.rows}

    @property
    def number_of_rows(self) -> int:
        """Number of rows in the table

        Returns
        -------
        int
            The number of rows
        """
        return len(self.rows)

    def total_sales(self, order_type: Optional[str] = None) -> float:
        """The sum of the sales price converted into GBP

        Parameters
        ----------
        order_type : Optional[str], optional
            [description], by default None

        Returns
        -------
        float
            the sum of the converted sales
        """
        if order_type is None:
            order_types = ["New", "Retread", "Not Specified"]
        else:
            order_types = [order_type]

        return sum(
            row.converted_amount for row in self.rows if row.order_type in order_types
        )
