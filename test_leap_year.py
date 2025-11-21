import unittest
from leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    """Test cases for the is_leap_year function."""
    
    def test_year_divisible_by_400(self):
        """Years divisible by 400 are leap years."""
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(2400))
    
    def test_year_divisible_by_100_not_400(self):
        """Years divisible by 100 but not 400 are not leap years."""
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(1800))
        self.assertFalse(is_leap_year(2100))
    
    def test_year_divisible_by_4_not_100(self):
        """Years divisible by 4 but not 100 are leap years."""
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2016))
        self.assertTrue(is_leap_year(2012))
    
    def test_year_not_divisible_by_4(self):
        """Years not divisible by 4 are not leap years."""
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(2022))
        self.assertFalse(is_leap_year(2021))
        self.assertFalse(is_leap_year(2019))
    
    def test_common_leap_years(self):
        """Test some well-known leap years."""
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2008))
    
    def test_common_non_leap_years(self):
        """Test some well-known non-leap years."""
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2001))
        self.assertFalse(is_leap_year(2100))


if __name__ == '__main__':
    unittest.main()
