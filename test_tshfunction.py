import pytest


@pytest.mark.parametrize("test_string, expected", [
    ("TSH,1.0,2.5,4.0,3.5,0.5", "Hyperthyroidism"),
    ("TSH,3.0,2. ,  1.8", "Normal Thyroid Funciton"),
    ("TSH,1.4,3.6,4.2,4.6,1.0", "Hypothyroidism"),
    ("TSH,.3, 1.9, 3.2, 0.4", "Hyperthyroidism"),
    ("TSH,3.4, 2.5, 1.7, 2.0", "Normal Thyroid Funciton"),
])
def test_diagnosis(test_string, expected):
    """ Test_Diagnosis Function

    Using a parametrized test, test_tshfunction.py
    tests the diagnosis function for it's ability to
    deal with TSH Value lists with different lengths,
    spacing, and decimal formatsself.

    :param: test_strings

    :returns: pass/fail test results"""

    from tshfunction import diagnosis

    answer = diagnosis(test_string)
    assert answer == expected
