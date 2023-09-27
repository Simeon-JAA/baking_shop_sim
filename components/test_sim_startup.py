"""Testing file for sim_startup"""

import pytest


from component_classes import Cupcake


def test_cupcake_class_works():
    """Tests creating a cupcake object works"""

    chocolate_cupcake = Cupcake("Chocolate", 5, 10)

    assert isinstance(chocolate_cupcake, Cupcake)


def test_cupcake_class_formats_name():
    """Tests creating a cupcake object formats the name"""

    chocolate_cake = Cupcake("chocolate", 5, 10)

    assert chocolate_cake.name == "Chocolate Cupcake"


def test_cupcake_class_formats_name_removes_spaces():
    """Tests creating a cupcake object formats the name by removing excess spaces"""

    chocolate_cake = Cupcake("   chocolate    ", 5, 10)

    assert chocolate_cake.name == "Chocolate Cupcake"


def test_cupcake_class_exception_raised_for_negative_price():
    """Tests exception raised with negative price input"""

    with pytest.raises(Exception):
        Cupcake("chocolate", -5, 10)


def test_cupcake_class_exception_raised_for_negative_amount():
    """Tests exception raised with negative amount input"""

    with pytest.raises(Exception):
        Cupcake("chocolate", 0, -1)


def test_cupcake_class_exception_raised_for_wrong_int_types_price():
    """Tests exception raised with wrong integer type input"""

    with pytest.raises(Exception):
        Cupcake("chocolate", "1", -1)


def test_cupcake_class_exception_raised_for_wrong_int_types_amount():
    """Tests exception raised with wrong integer type input"""

    with pytest.raises(Exception):
        Cupcake("chocolate", 1, "-1")
