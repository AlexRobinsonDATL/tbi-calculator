import pytest
from fake import FakeModel, FakeView


@pytest.fixture
def fake_model():
    return FakeModel()


@pytest.fixture
def fake_view():
    return FakeView()
