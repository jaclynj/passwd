from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from pytest import raises

from passwd import PasswordGenerator


def test_length():
    all_8 = PasswordGenerator(8)
    assert len(all_8) == 8
    assert len(all_8.generate()) == 8

    all_10 = PasswordGenerator(10)
    assert len(all_10) == 10
    assert len(all_10.generate()) == 10

    all_0 = PasswordGenerator(0)
    assert len(all_0) == 0
    assert len(all_0.generate()) == 0


def test_strange_values():
    negative_1 = PasswordGenerator(-1)
    assert len(negative_1.generate()) == 0

    # len() is required to return >= 0
    assert len(negative_1) == 0

    upper_yes = PasswordGenerator(64, uppercase="yes")
    assert len(upper_yes) == 64
    assert len(upper_yes.generate()) == 64

    # Assert there is at least one uppercase char in a long password
    assert sum(1 for char in upper_yes.generate() if char in ascii_uppercase) > 0

    lower_0 = PasswordGenerator(64, lowercase=0)
    assert len(lower_0) == 64
    assert len(lower_0.generate()) == 64

    # Assert there are no lowercase chars in a long password
    assert sum(1 for char in lower_0.generate() if char in ascii_lowercase) == 0


def test_exclusions():
    no_special_8 = PasswordGenerator(8, special=False)
    for char in punctuation:
        assert char not in no_special_8.generate()

    no_upper_10 = PasswordGenerator(10, uppercase=False)
    for char in ascii_uppercase:
        assert char not in no_upper_10.generate()

    no_lower_7 = PasswordGenerator(7, lowercase=False)
    for char in ascii_lowercase:
        assert char not in no_lower_7.generate()

    no_digits_16 = PasswordGenerator(16, digits=False)
    for char in digits:
        assert char not in no_digits_16.generate()
