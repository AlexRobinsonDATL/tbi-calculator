import pytest

from tbi_calculator.controller import Controller


@pytest.fixture
def controller(fake_model, fake_view):
    return Controller(view=fake_view, model=fake_model)


@pytest.mark.unittest
def test_controller_constructor(controller):
    assert isinstance(controller, Controller)


@pytest.mark.unittest
def test_controller_start(controller):
    controller.start()
    assert controller.view.is_setup is True
    assert controller.view.is_looping is True


@pytest.mark.unittest
def test_controller_execute(controller):
    controller.second_thread()
    assert controller.model.data == [1, 2, 3]
    assert controller.model.is_filtered is True
