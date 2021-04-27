import json
from datetime import datetime
from pathlib import Path

import pytest

from tbi_calculator.model.datastructures import TBIRow, TBITable


@pytest.fixture
def tbi_row():
    return TBIRow(
        customer_order="N000019522",
        line_release="4/0",
        customer_code="B010662",
        customer_name="I AM A CUSTOMER",
        item="DR11111T-2",
        description=None,
        qty_ordered=35,
        to_credit=0,
        to_invoice=35,
        qty_shipped=35,
        qty_invoiced=0,
        amount=36015,
        um="EA",
        tci="*",
        release_note="N048151",
        release_date=datetime(2020, 4, 13, 0),
        sales_person=None,
        currency_code="USD",
        converted_amount=27703.85,
    )


@pytest.fixture(scope="session")
def metabase_response():
    with open(Path(__file__).parent / "tbi_example_data.json", "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def tbitable(metabase_response):
    return TBITable(metabase_response)


def test_tbirow_constructor(tbi_row):
    assert isinstance(tbi_row, TBIRow)


@pytest.mark.parametrize(
    ("customer_order", "expected_result"),
    [("N000019522", "New"), ("R000042526", "Retread"), ("U000042526", "Not Specified")],
)
def test_tbirow_order_type(tbi_row, customer_order, expected_result):
    row = tbi_row
    row.customer_order = customer_order
    assert row.order_type == expected_result


@pytest.mark.parametrize(
    ("customer", "customer_name", "expected_result"),
    [
        ("B010662", "DUNLOP ATLAS", True),
        ("D086000", "CUSTOMER", True),
        ("D085000", "CUSTOMER", True),
        ("B010662", "I AM A CUSTOMER", False),
    ],
)
def test_tbirow_is_dunlop(tbi_row, customer, customer_name, expected_result):
    row = tbi_row
    row.customer_code = customer
    row.customer_name = customer_name
    assert row.is_dunlop() is expected_result


def test_tbitable_constructor(metabase_response):
    table = TBITable(metabase_response)
    assert isinstance(table, TBITable)


@pytest.mark.parametrize(
    ("order_type", "expected_result"),
    [
        (None, 909013.61),
        ("New", 872752.04),
        ("Retread", 36261.57),
    ],
)
def test_tbitable_total_sales(tbitable, order_type, expected_result):
    assert tbitable.total_sales(order_type) == pytest.approx(expected_result)


def test_tbitable_excludes_customer_codes(tbitable):
    exclusions = ["U030028", "P030600"]
    tbitable.exclude(exclusions)
    assert set(exclusions).issubset(tbitable.customer_codes) is False
