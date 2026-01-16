import datetime

def next_repeating_calendar(year):
    original = datetime.date(year, 1, 1)
    is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    next_year = year + 1

    while True:
        candidate = datetime.date(next_year, 1, 1)
        candidate_is_leap = (next_year % 4 == 0 and (next_year % 100 != 0 or next_year % 400 == 0))

        # Must match both weekday and leap-status
        if candidate.weekday() == original.weekday() and candidate_is_leap == is_leap:
            return next_year

        next_year += 1

# Example usage:
year = 2015
print(f"The next year with the same calendar as {year} is {next_repeating_calendar(year)}.")