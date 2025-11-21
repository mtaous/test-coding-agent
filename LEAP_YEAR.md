# Leap Year Function

This module provides a function to determine if a given year is a leap year.

## Usage

```python
from leap_year import is_leap_year

# Check if a year is a leap year
print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```

## Leap Year Rules

A leap year is:
- Divisible by 4, AND
- If divisible by 100, it must also be divisible by 400

Examples:
- 2000 is a leap year (divisible by 400)
- 1900 is NOT a leap year (divisible by 100 but not 400)
- 2024 is a leap year (divisible by 4 but not 100)
- 2023 is NOT a leap year (not divisible by 4)

## Running Tests

Run the test suite:

```bash
python3 -m unittest test_leap_year.py
```

Or with verbose output:

```bash
python3 -m unittest test_leap_year.py -v
```
