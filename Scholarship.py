"""
Task 1: Student Scholarship Eligibility System
Topic: Conditional Statements (if, elif, else)
"""

# Eligibility thresholds (easy to change in one place)
MIN_MARKS = 80
FULL_SCHOLARSHIP_MARKS = 90
MIN_ATTENDANCE = 85
MAX_INCOME = 50000


def get_name():
    """Ask for the student's name until a non-empty, valid name is entered."""
    while True:
        name = input("Enter student name: ").strip()
        # Allow letters and spaces only
        if name and name.replace(" ", "").isalpha():
            return name
        print("Invalid name. Please use letters and spaces only.")


def get_number(prompt, minimum, maximum=None):
    """Ask for a number until it is valid and within the allowed range."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if value < minimum or (maximum is not None and value > maximum):
            if maximum is not None:
                print(f"Value must be between {minimum} and {maximum}.")
            else:
                print(f"Value must be {minimum} or more.")
            continue
        return value


def main():
    print("=" * 50)
    print("   STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 50)

    # 1 & 2. Collect and validate input
    name = get_name()
    marks = get_number("Enter academic marks (%): ", 0, 100)
    attendance = get_number("Enter attendance percentage (%): ", 0, 100)
    income = get_number("Enter monthly family income (Rs.): ", 0)

    # 3. Check each criterion separately and collect reasons for failure
    reasons = []
    if marks < MIN_MARKS:
        reasons.append(f"Marks are below the required {MIN_MARKS}%.")
    if attendance < MIN_ATTENDANCE:
        reasons.append(f"Attendance is below the required {MIN_ATTENDANCE}%.")
    if income > MAX_INCOME:
        reasons.append(f"Monthly family income exceeds Rs. {MAX_INCOME:,}.")

    # 4 & 5. Decide the result
    if not reasons:
        eligible = True
        if marks >= FULL_SCHOLARSHIP_MARKS:
            result = "Full Scholarship"
        else:  # marks are 80 or more but below 90
            result = "Partial Scholarship"
    else:
        eligible = False
        result = "Not Eligible"

    # 6. Final report
    print("\n" + "=" * 50)
    print("        SCHOLARSHIP EVALUATION REPORT")
    print("=" * 50)
    print(f"Student Name      : {name}")
    print(f"Academic Marks    : {marks:.2f}%  (min {MIN_MARKS}%)")
    print(f"Attendance        : {attendance:.2f}%  (min {MIN_ATTENDANCE}%)")
    print(f"Monthly Income    : Rs. {income:,.2f}  (max Rs. {MAX_INCOME:,})")
    print("-" * 50)
    print(f"Eligibility       : {'ELIGIBLE' if eligible else 'NOT ELIGIBLE'}")
    print(f"Result            : {result}")
    if not eligible:
        print("Reason(s):")
        for reason in reasons:
            print(f"  - {reason}")
    print("=" * 50)


if __name__ == "__main__":
    main()
    