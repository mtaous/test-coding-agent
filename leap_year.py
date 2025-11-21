def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    A leap year is:
    - Divisible by 4, AND
    - If divisible by 100, it must also be divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
        
    Examples:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2023)
        False
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
