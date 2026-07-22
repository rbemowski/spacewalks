import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    assert text_to_duration("10:20") == pytest.approx(10.333333)
