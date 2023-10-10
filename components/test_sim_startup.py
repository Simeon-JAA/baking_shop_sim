"""Testing file for sim_startup"""

import pytest


from component_classes import Cupcake
from sim_startup import check_user_email


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


def test_check_user_email_base_case_not_email():
    """Tests base case for function check_user_email"""

    with pytest.raises(Exception):
        check_user_email("this is not an email")


def test_check_user_email_base_case_invalid_email():
    """Tests base case for function check_user_email"""

    with pytest.raises(Exception):
        check_user_email("invalid?email@??.com")


def test_check_user_email_base_case_invalid_email_contains_spaces():
    """Tests base case for function check_user_email"""

    with pytest.raises(Exception):
        check_user_email("test email@gmail.com")


def test_check_user_email_base_case_invalid_email_contains_invalid_characters_1():
    """Tests base case for function check_user_email"""

    with pytest.raises(Exception):
        check_user_email("example?@gmail.com")


def test_check_user_email_base_case_invalid_email_contains_invalid_characters_2():
    """Tests base case for function check_user_email"""

    with pytest.raises(Exception):
        check_user_email("example@g?mail.com")


def test_check_user_email_base_case_valid_email_1():
    """Tests base case for valid email in function check_user_email"""

    result = check_user_email("test_email_1@gmail.com")

    assert result == True


def test_check_user_email_base_case_valid_email_2():
    """Tests base case for valid email in function check_user_email"""

    result = check_user_email("test_email_1@gmail.co.uk")

    assert result == True


def test_check_user_email_base_case_valid_email_2():
    """Tests base case for valid email in function check_user_email"""

    result = check_user_email("test-emai_123@company.ac.uk")

    assert result == True


def test_check_user_email_base_case_valid_email_3():
    """Tests base case for valid email in function check_user_email"""

    result = check_user_email("test-emai_123@company.org")

    assert result == True


def test_check_user_email_base_case_valid_email_4():
    """Tests base case for valid email in function check_user_email"""

    result = check_user_email(" test-emai_123@outlook.co.uk ")

    assert result == True
