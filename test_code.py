from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    assert abs(text_to_duration("10:20") - 10.333333) < 1e-5


test_text_to_duration_integer()
test_text_to_duration_float()
test_text_to_duration_irrational()
