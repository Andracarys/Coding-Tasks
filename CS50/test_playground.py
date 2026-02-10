from playground import CalculateDate
from datetime import date

def test_calc():
    valid_dob = CalculateDate(date(1990,4,21))
    assert valid_dob.dob.year == 1990
    assert valid_dob.dob.month == 4
    assert valid_dob.dob.day == 21

# run on terminal = pytest "name of the file"