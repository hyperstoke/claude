from run_at_format_check import is_valid_run_at


def test_correct_times_are_accepted():
    assert is_valid_run_at("09:05") is True
    assert is_valid_run_at("00:00") is True
    assert is_valid_run_at("23:59") is True


def test_wrong_length_is_rejected():
    assert is_valid_run_at("") is False
    assert is_valid_run_at("9:05") is False
    assert is_valid_run_at("09:050") is False


def test_wrong_separator_is_rejected():
    assert is_valid_run_at("09-05") is False
    assert is_valid_run_at("090:5") is False


def test_letters_instead_of_digits_are_rejected():
    assert is_valid_run_at("0a:05") is False
    assert is_valid_run_at("09:b5") is False


def test_out_of_range_is_rejected():
    assert is_valid_run_at("24:00") is False
    assert is_valid_run_at("09:60") is False
    assert is_valid_run_at("99:99") is False
