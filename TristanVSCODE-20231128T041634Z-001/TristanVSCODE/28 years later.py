# Tristan Perez
# 28 Leap Year Checker

# int
# function

def is_leap_year(year):
    y = year
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

# Main
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2022))  # Expected output: False
print(is_leap_year(2024))  # Expected output: True
