"""Testing file for component_classes"""

import pytest


from component_classes import User


def test_class_user_default_good_luck():
    """Tests default good luck stat is 10 for user class"""

    result = User("example_user")

    assert result.good_luck == 10


def test_class_user_default_bad_luck():
    """Tests default bad luck stat is 0 for user class"""

    result = User("example_user")

    assert result.bad_luck == 0


def test_class_user_default_level():
    """Tests default level is 1 for a new user"""

    result = User("example_user")

    assert result.level == 1


def test_class_user_default_xp():
    """Tests default xp for a new user is 0"""

    result = User("example_user")

    assert result.xp == 0


def test_class_user_check_valid_email_spaces():
    """Tests email validator for creating user using regex"""

    with pytest.raises(Exception):
        User("simeon", "This is not an email")


def test_class_user_check_invalid_email_exception_1():
    """Tests email validator for creating user using regex"""

    with pytest.raises(Exception):
        User("simeon", "invalid_email.com")


def test_class_user_check_invalid_email_exception_2():
    """Tests email validator for creating user using regex"""

    with pytest.raises(Exception):
        User("simeon", "invalid_email.com.co.uk")


def test_class_user_email_validated_using_regex():
    """Tests email validator for creating user using regex"""

    result = User("example", "example@example.co.uk")

    assert result.email == "example@example.co.uk"


def test_class_user_invalid_username_trailing_space():
    """Tests username validator for creating user using regex"""

    with pytest.raises(Exception):
        User("example ")


def test_class_user_invalid_username_contains_spaces():
    """Tests username validator for creating user using regex"""

    with pytest.raises(Exception):
        User("exa mp  le  s")


def test_class_user_invalid_username_too_short():
    """Tests username validator for creating user using regex"""

    with pytest.raises(Exception):
        User("seb")


def test_class_user_invalid_username_too_long():
    """Tests username validator for creating user using regex"""

    with pytest.raises(Exception):
        User("sebdimouedoigyhwbisuyb")


def test_class_user_increase_good_luck_works():
    """Tests increasing the good luck stat works"""

    example = User("Example")
    luck_stat_start = example.good_luck
    example.alter_good_luck(19)

    assert luck_stat_start < example.good_luck


def test_class_user_increase_good_luck_limited_to_max():
    """Tests increasing the good luck stat is limited to max luck stat"""

    example = User("Example")
    example.alter_good_luck(1000)

    assert example.good_luck == example.max_luck


def test_class_user_increase_good_limited_to_0():
    """Tests decreasing the good luck stat is limited to 0"""

    example = User("Example")
    example.alter_good_luck(-5000)

    assert example.good_luck == 0


def test_class_user_increase_bad_luck_works():
    """Tests increasing the bad luck stat works"""

    example = User("Example")
    luck_stat_start = example.bad_luck
    example.alter_bad_luck(19)

    assert luck_stat_start < example.bad_luck


def test_class_user_increase_bad_luck_limited_to_max():
    """Tests increasing the bad luck stat is limited to max luck stat"""

    example = User("Example")
    example.alter_bad_luck(1000)

    assert example.bad_luck == example.max_luck


def test_class_user_increase_bad_limited_to_0():
    """Tests decreasing the bad luck stat is limited to 0"""

    example = User("Example")
    example.alter_bad_luck(-5000)

    assert example.bad_luck == 0
