from datetime import date, datetime


def calculate_age_in_days(dob_str):
    """
    Calculates age in days based on date of birth.

    Parameters:
    dob_str (str): Date of birth in YYYY-MM-DD format

    Returns:
    int: Age in days
    """
    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    today = date.today()
    return (today - dob).days


def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    days_old = calculate_age_in_days(dob_input)
    print(f"You are {days_old} days old.")


if __name__ == "__main__":
    main()
