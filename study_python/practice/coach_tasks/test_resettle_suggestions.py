from resettle_suggestions import resettle_suggestions


def test_almost_sorted_gets_fixed_in_place():
    hits = [30, 10, 20]
    same_list = hits
    assert resettle_suggestions(hits) is True
    assert hits == [30, 20, 10]
    assert same_list is hits


def test_already_sorted_reports_no_move():
    hits = [30, 20, 10]
    assert resettle_suggestions(hits) is False
    assert hits == [30, 20, 10]


def test_reversed_list_is_sorted_and_reports_move():
    hits = [10, 20, 30]
    assert resettle_suggestions(hits) is True
    assert hits == [30, 20, 10]


def test_empty_and_single_do_not_crash():
    assert resettle_suggestions([]) is False
    assert resettle_suggestions([50]) is False


def test_equal_values_report_no_move():
    hits = [15, 15, 15]
    assert resettle_suggestions(hits) is False
    assert hits == [15, 15, 15]
