import unittest
from datetime import datetime, date

from CodeClub.DateAndTime.get_age import get_age


class TestAge(unittest.TestCase):
    def testCurrentDate(self):
        assert get_age(date(year=1985, month=3, day=12)) == 38
        assert get_age(date(year=1990, month=3, day=12)) == 33

    def testVariousDate(self):
        assert get_age(date(year=1985, month=3, day=12), date(year=1995, month=3, day=11)) == 9