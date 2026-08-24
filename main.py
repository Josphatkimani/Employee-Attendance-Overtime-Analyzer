# ============================================================
# Employee Attendance and Overtime Analyser
# MSc Fundamentals of Programming - Capstone Project
# ============================================================


# ------------------------------------------------------------
# 1. Employee data
# ------------------------------------------------------------

EMPLOYEE_RECORDS = [
    {
        "employee_id": "E001",
        "employee_name": "Jane Wanjiku",
        "department": "Finance",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 20,
        "leave_days": 2,
        "hours_worked": 176,
        "hourly_rate": 850
    },
    {
        "employee_id": "E002",
        "employee_name": "Brian Otieno",
        "department": "IT",
        "employment_type": "full time",
        "days_expected": 22,
        "days_present": 19,
        "leave_days": 1,
        "hours_worked": 185,
        "hourly_rate": 920
    },
    {
        "employee_id": "E003",
        "employee_name": "Amina Hassan",
        "department": "Human Resources",
        "employment_type": "Part-time",
        "days_expected": 20,
        "days_present": 17,
        "leave_days": 2,
        "hours_worked": 88,
        "hourly_rate": 700
    },
    {
        "employee_id": "E004",
        "employee_name": "Peter Mwangi",
        "department": "Operations",
        "employment_type": "Contract",
        "days_expected": 22,
        "days_present": 18,
        "leave_days": 0,
        "hours_worked": 146,
        "hourly_rate": 780
    },
    {
        "employee_id": "E005",
        "employee_name": "Lucy Njeri",
        "department": "Sales",
        "employment_type": "FULL-TIME",
        "days_expected": 22,
        "days_present": 21,
        "leave_days": 1,
        "hours_worked": 168,
        "hourly_rate": 810
    },
    {
        "employee_id": "E006",
        "employee_name": "David Kiptoo",
        "department": "Operations",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 16,
        "leave_days": 1,
        "hours_worked": 172,
        "hourly_rate": 760
    },
    {
        "employee_id": "E007",
        "employee_name": "Faith Atieno",
        "department": "Finance",
        "employment_type": "part time",
        "days_expected": 20,
        "days_present": 19,
        "leave_days": 1,
        "hours_worked": 92,
        "hourly_rate": 680
    },
    {
        "employee_id": "E008",
        "employee_name": "Samuel Kariuki",
        "department": "IT",
        "employment_type": "Contract",
        "days_expected": 22,
        "days_present": 22,
        "leave_days": 0,
        "hours_worked": 132,
        "hourly_rate": 880
    },
    {
        "employee_id": "E009",
        "employee_name": "Mercy Chebet",
        "department": "Sales",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 18,
        "leave_days": 2,
        "hours_worked": 158,
        "hourly_rate": 790
    },
    {
        "employee_id": "E010",
        "employee_name": "John Kamau",
        "department": "Human Resources",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 20,
        "leave_days": 1,
        "hours_worked": 164,
        "hourly_rate": 820
    },
    {
        "employee_id": "E011",
        "employee_name": "Rose Achieng",
        "department": "Operations",
        "employment_type": "Contract",
        "days_expected": 22,
        "days_present": 21,
        "leave_days": 1,
        "hours_worked": 151,
        "hourly_rate": 740
    },
    {
        "employee_id": "E012",
        "employee_name": "Kevin Mutua",
        "department": "IT",
        "employment_type": "Part-time",
        "days_expected": 20,
        "days_present": 15,
        "leave_days": 1,
        "hours_worked": 78,
        "hourly_rate": 710
    },
    {
        "employee_id": "E013",
        "employee_name": "Grace Wambui",
        "department": "Finance",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 23,
        "leave_days": 0,
        "hours_worked": 170,
        "hourly_rate": 860
    },
    {
        "employee_id": "E014",
        "employee_name": "Allan Musyoka",
        "department": "Sales",
        "employment_type": "Intern",
        "days_expected": 22,
        "days_present": 19,
        "leave_days": 1,
        "hours_worked": 162,
        "hourly_rate": 620
    },
    {
        "employee_id": "E015",
        "employee_name": "Esther Jepkoech",
        "department": "Operations",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 18,
        "leave_days": 2,
        "hours_worked": -5,
        "hourly_rate": 770
    },
    {
        "employee_id": None,
        "employee_name": "Mohamed Noor",
        "department": "IT",
        "employment_type": "Contract",
        "days_expected": 22,
        "days_present": 20,
        "leave_days": 1,
        "hours_worked": 128,
        "hourly_rate": 900
    },
    {
        "employee_id": "E017",
        "employee_name": "Irene Muthoni",
        "department": None,
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 21,
        "leave_days": 0,
        "hours_worked": 166,
        "hourly_rate": 830
    },
    {
        "employee_id": "E018",
        "employee_name": "Collins Ouma",
        "department": "Sales",
        "employment_type": "Part-time",
        "days_expected": 20,
        "days_present": 17,
        "leave_days": 1,
        "hours_worked": 86,
        "hourly_rate": 0
    },
    {
        "employee_id": "E019",
        "employee_name": "Diana Wafula",
        "department": "Finance",
        "employment_type": "Contract",
        "days_expected": 22,
        "days_present": 17,
        "leave_days": 3,
        "hours_worked": 124,
        "hourly_rate": 795
    },
    {
        "employee_id": "E020",
        "employee_name": "Joseph Maina",
        "department": "IT",
        "employment_type": "Full-time",
        "days_expected": 22,
        "days_present": 21,
        "leave_days": 1,
        "hours_worked": 194,
        "hourly_rate": 950
    }
]


# ------------------------------------------------------------
# 2. Constants
# ------------------------------------------------------------

STANDARD_HOURS = {
    "Full-time": 160,
    "Part-time": 80,
    "Contract": 120
}

OVERTIME_MULTIPLIER = 1.5


# ------------------------------------------------------------
# 3. Employment type standardisation
# ------------------------------------------------------------

def standardise_employment_type(employment_type):
    """
    Standardise obvious variations in employment type.

    Values such as 'full time', 'FULL-TIME' and 'part time'
    represent the same employment categories as the recognised
    values.
    """

    if not isinstance(employment_type, str):
        return None

    value = employment_type.strip().lower()

    mappings = {
        "full-time": "Full-time",
        "full time": "Full-time",
        "part-time": "Part-time",
        "part time": "Part-time",
        "contract": "Contract"
    }

    return mappings.get(value)


# ------------------------------------------------------------
# 4. Validate one employee record
# ------------------------------------------------------------

def validate_record(record):
    """
    Validate an individual employee record.

    Returns:
        A list containing all validation errors.
    """

    errors = []

    if not record.get("employee_id"):
        errors.append("Employee ID is missing.")

    if not record.get("employee_name"):
        errors.append("Employee name is missing.")

    if not record.get("department"):
        errors.append("Department is missing.")

    days_expected = record.get("days_expected")
    days_present = record.get("days_present")
    leave_days = record.get("leave_days")
    hours_worked = record.get("hours_worked")
    hourly_rate = record.get("hourly_rate")

    if days_expected is None or days_expected <= 0:
        errors.append("Expected days must be greater than zero.")

    if days_present is None or days_present < 0:
        errors.append("Present days cannot be negative.")

    if leave_days is None or leave_days < 0:
        errors.append("Leave days cannot be negative.")

    if (
        days_expected is not None
        and days_present is not None
        and leave_days is not None
        and days_present + leave_days > days_expected
    ):
        errors.append(
            "Present days plus leave days cannot exceed expected days."
        )

    if hours_worked is None or hours_worked < 0:
        errors.append("Hours worked cannot be negative.")

    if hourly_rate is None or hourly_rate <= 0:
        errors.append("Hourly rate must be greater than zero.")

    standardised_type = standardise_employment_type(
        record.get("employment_type")
    )

    if standardised_type is None:
        errors.append("Employment type is not recognised.")

    return errors


# ------------------------------------------------------------
# 5. Validate all records
# ------------------------------------------------------------

def validate_all_records(records):
    """
    Validate all supplied employee records.

    Returns:
        valid_records
        invalid_records
    """

    valid_records = []
    invalid_records = []

    for record in records:

        errors = validate_record(record)

        if errors:
            invalid_records.append({
                "record": record,
                "reasons": errors
            })
        else:
            valid_record = record.copy()

            valid_record["employment_type"] = (
                standardise_employment_type(
                    record["employment_type"]
                )
            )

            valid_records.append(valid_record)

    return valid_records, invalid_records


# ------------------------------------------------------------
# 6. Attendance calculations
# ------------------------------------------------------------

def calculate_attendance(record):
    """
    Calculate absence days, attendance percentage
    and attendance category.
    """

    expected = record["days_expected"]
    present = record["days_present"]
    leave = record["leave_days"]

    absence_days = expected - present - leave

    attendance_percentage = (
        (present + leave) / expected
    ) * 100

    if attendance_percentage >= 95:
        category = "Excellent"
    elif attendance_percentage >= 85:
        category = "Satisfactory"
    else:
        category = "Needs improvement"

    return {
        "absence_days": absence_days,
        "attendance_percentage": attendance_percentage,
        "attendance_category": category
    }


# ------------------------------------------------------------
# 7. Overtime and payment calculations
# ------------------------------------------------------------

def calculate_overtime(record):
    """
    Calculate standard hours, overtime hours,
    regular payment, overtime payment and total payment.
    """

    employment_type = record["employment_type"]

    standard_hours = STANDARD_HOURS[employment_type]

    hours_worked = record["hours_worked"]
    hourly_rate = record["hourly_rate"]

    overtime_hours = hours_worked - standard_hours

    if overtime_hours < 0:
        overtime_hours = 0

    regular_hours = min(hours_worked, standard_hours)

    regular_payment = regular_hours * hourly_rate

    overtime_payment = (
        overtime_hours
        * hourly_rate
        * OVERTIME_MULTIPLIER
    )

    total_payment = regular_payment + overtime_payment

    return {
        "standard_hours": standard_hours,
        "overtime_hours": overtime_hours,
        "regular_payment": regular_payment,
        "overtime_payment": overtime_payment,
        "total_payment": total_payment
    }


# ------------------------------------------------------------
# 8. Prepare calculated employee records
# ------------------------------------------------------------

def prepare_records(valid_records):
    """
    Add attendance, overtime and payment calculations
    to every valid employee record.
    """

    prepared_records = []

    for record in valid_records:

        employee = record.copy()

        attendance = calculate_attendance(employee)
        overtime = calculate_overtime(employee)

        employee.update(attendance)
        employee.update(overtime)

        prepared_records.append(employee)

    return prepared_records


# ------------------------------------------------------------
# 9. View all valid employee records
# ------------------------------------------------------------

def view_valid_records(records):

    if not records:
        print("\nNo valid employee records available.")
        return

    print("\n" + "=" * 100)
    print("VALID EMPLOYEE RECORDS")
    print("=" * 100)

    for employee in records:

        print(f"\nEmployee ID: {employee['employee_id']}")
        print(f"Name: {employee['employee_name']}")
        print(f"Department: {employee['department']}")
        print(f"Employment Type: {employee['employment_type']}")
        print(f"Expected Days: {employee['days_expected']}")
        print(f"Present Days: {employee['days_present']}")
        print(f"Leave Days: {employee['leave_days']}")
        print(f"Absence Days: {employee['absence_days']}")
        print(
            f"Attendance: "
            f"{employee['attendance_percentage']:.2f}%"
        )
        print(
            f"Attendance Category: "
            f"{employee['attendance_category']}"
        )
        print(f"Hours Worked: {employee['hours_worked']}")
        print(f"Standard Hours: {employee['standard_hours']}")
        print(f"Overtime Hours: {employee['overtime_hours']:.2f}")
        print(f"Hourly Rate: {employee['hourly_rate']:.2f}")
        print(
            f"Regular Payment: "
            f"{employee['regular_payment']:.2f}"
        )
        print(
            f"Overtime Payment: "
            f"{employee['overtime_payment']:.2f}"
        )
        print(
            f"Total Payment: "
            f"{employee['total_payment']:.2f}"
        )
        print("-" * 100)


# ------------------------------------------------------------
# 10. Search for an employee
# ------------------------------------------------------------

def search_employee(records):

    search_value = input(
        "\nEnter employee ID or name: "
    ).strip().lower()

    found = False

    for employee in records:

        employee_id = employee["employee_id"].lower()
        employee_name = employee["employee_name"].lower()

        if (
            search_value == employee_id
            or search_value == employee_name
        ):
            print("\nEmployee found:")
            print(f"Employee ID: {employee['employee_id']}")
            print(f"Name: {employee['employee_name']}")
            print(f"Department: {employee['department']}")
            print(
                f"Employment Type: "
                f"{employee['employment_type']}"
            )
            print(
                f"Attendance: "
                f"{employee['attendance_percentage']:.2f}%"
            )
            print(
                f"Attendance Category: "
                f"{employee['attendance_category']}"
            )
            print(f"Overtime Hours: {employee['overtime_hours']:.2f}")
            print(
                f"Overtime Payment: "
                f"{employee['overtime_payment']:.2f}"
            )
            print(
                f"Total Payment: "
                f"{employee['total_payment']:.2f}"
            )

            found = True
            break

    if not found:
        print("\nEmployee not found.")


# ------------------------------------------------------------
# 11. Analyse employee attendance
# ------------------------------------------------------------

def analyse_attendance(records):

    if not records:
        print("\nNo valid records available.")
        return

    print("\n" + "=" * 70)
    print("EMPLOYEE ATTENDANCE ANALYSIS")
    print("=" * 70)

    for employee in records:

        print(
            f"{employee['employee_id']} - "
            f"{employee['employee_name']}: "
            f"{employee['attendance_percentage']:.2f}% "
            f"({employee['attendance_category']})"
        )

    highest = max(
        employee["attendance_percentage"]
        for employee in records
    )

    lowest = min(
        employee["attendance_percentage"]
        for employee in records
    )

    highest_employees = [
        employee["employee_name"]
        for employee in records
        if employee["attendance_percentage"] == highest
    ]

    lowest_employees = [
        employee["employee_name"]
        for employee in records
        if employee["attendance_percentage"] == lowest
    ]

    print("\nHighest Attendance:")
    print(f"{highest:.2f}% - {', '.join(highest_employees)}")

    print("\nLowest Attendance:")
    print(f"{lowest:.2f}% - {', '.join(lowest_employees)}")


# ------------------------------------------------------------
# 12. Employees requiring attendance improvement
# ------------------------------------------------------------

def view_attendance_improvement(records):

    employees = [
        employee
        for employee in records
        if employee["attendance_category"]
        == "Needs improvement"
    ]

    print("\n" + "=" * 70)
    print("EMPLOYEES REQUIRING ATTENDANCE IMPROVEMENT")
    print("=" * 70)

    if not employees:
        print("No employees require attendance improvement.")
        return

    for employee in employees:

        print(
            f"{employee['employee_id']} - "
            f"{employee['employee_name']} | "
            f"Attendance: "
            f"{employee['attendance_percentage']:.2f}% | "
            f"Absence Days: {employee['absence_days']}"
        )


# ------------------------------------------------------------
# 13. Analyse overtime
# ------------------------------------------------------------

def analyse_overtime(records):

    if not records:
        print("\nNo valid records available.")
        return

    print("\n" + "=" * 90)
    print("OVERTIME AND PAYMENT ANALYSIS")
    print("=" * 90)

    for employee in records:

        print(
            f"{employee['employee_id']} - "
            f"{employee['employee_name']} | "
            f"Overtime: {employee['overtime_hours']:.2f} hours | "
            f"Overtime Payment: "
            f"{employee['overtime_payment']:.2f} | "
            f"Total Payment: "
            f"{employee['total_payment']:.2f}"
        )

    maximum_overtime = max(
        employee["overtime_hours"]
        for employee in records
    )

    maximum_overtime_payment = max(
        employee["overtime_payment"]
        for employee in records
    )

    maximum_total_payment = max(
        employee["total_payment"]
        for employee in records
    )

    most_overtime = [
        employee["employee_name"]
        for employee in records
        if employee["overtime_hours"]
        == maximum_overtime
    ]

    highest_overtime_payment = [
        employee["employee_name"]
        for employee in records
        if employee["overtime_payment"]
        == maximum_overtime_payment
    ]

    highest_total_payment = [
        employee["employee_name"]
        for employee in records
        if employee["total_payment"]
        == maximum_total_payment
    ]

    print("\nMost Overtime Hours:")
    print(
        f"{maximum_overtime:.2f} hours - "
        f"{', '.join(most_overtime)}"
    )

    print("\nHighest Overtime Payment:")
    print(
        f"{maximum_overtime_payment:.2f} - "
        f"{', '.join(highest_overtime_payment)}"
    )

    print("\nHighest Total Payment:")
    print(
        f"{maximum_total_payment:.2f} - "
        f"{', '.join(highest_total_payment)}"
    )


# ------------------------------------------------------------
# 14. Compare departments
# ------------------------------------------------------------

def compare_departments(records):

    if not records:
        print("\nNo valid records available.")
        return

    departments = {}

    for employee in records:

        department = employee["department"]

        if department not in departments:
            departments[department] = []

        departments[department].append(employee)

    department_results = []

    for department, employees in departments.items():

        total_attendance = sum(
            employee["attendance_percentage"]
            for employee in employees
        )

        average_attendance = (
            total_attendance / len(employees)
        )

        overtime_expenditure = sum(
            employee["overtime_payment"]
            for employee in employees
        )

        department_results.append({
            "department": department,
            "average_attendance": average_attendance,
            "overtime_expenditure": overtime_expenditure
        })

    print("\n" + "=" * 80)
    print("DEPARTMENT COMPARISON")
    print("=" * 80)

    for result in department_results:

        print(
            f"{result['department']}: "
            f"Average Attendance = "
            f"{result['average_attendance']:.2f}% | "
            f"Overtime Expenditure = "
            f"{result['overtime_expenditure']:.2f}"
        )

    highest_expenditure = max(
        result["overtime_expenditure"]
        for result in department_results
    )

    highest_departments = [
        result["department"]
        for result in department_results
        if result["overtime_expenditure"]
        == highest_expenditure
    ]

    print("\nDepartment with Highest Overtime Expenditure:")
    print(
        f"{', '.join(highest_departments)} "
        f"({highest_expenditure:.2f})"
    )


# ------------------------------------------------------------
# 15. View invalid records
# ------------------------------------------------------------

def view_invalid_records(invalid_records):

    print("\n" + "=" * 80)
    print("INVALID EMPLOYEE RECORDS")
    print("=" * 80)

    if not invalid_records:
        print("No invalid records found.")
        return

    for item in invalid_records:

        record = item["record"]

        print(
            f"\nEmployee ID: "
            f"{record.get('employee_id')}"
        )

        print(
            f"Employee Name: "
            f"{record.get('employee_name')}"
        )

        print(
            f"Department: "
            f"{record.get('department')}"
        )

        print("Reason(s):")

        for reason in item["reasons"]:
            print(f"  - {reason}")


# ------------------------------------------------------------
# 16. Organisational summary
# ------------------------------------------------------------

def organisational_summary(
    supplied_count,
    valid_records,
    invalid_records
):

    if not valid_records:
        print("\nNo valid records available.")
        return

    total_overtime = sum(
        employee["overtime_hours"]
        for employee in valid_records
    )

    average_overtime = (
        total_overtime / len(valid_records)
    )

    total_overtime_expenditure = sum(
        employee["overtime_payment"]
        for employee in valid_records
    )

    average_attendance = sum(
        employee["attendance_percentage"]
        for employee in valid_records
    ) / len(valid_records)

    excellent = sum(
        1
        for employee in valid_records
        if employee["attendance_category"] == "Excellent"
    )

    satisfactory = sum(
        1
        for employee in valid_records
        if employee["attendance_category"] == "Satisfactory"
    )

    needs_improvement = sum(
        1
        for employee in valid_records
        if employee["attendance_category"]
        == "Needs improvement"
    )

    unexplained_absences = sum(
        1
        for employee in valid_records
        if employee["absence_days"] > 0
    )

    print("\n" + "=" * 80)
    print("ORGANISATIONAL SUMMARY")
    print("=" * 80)

    print(f"Supplied records: {supplied_count}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Invalid records: {len(invalid_records)}")

    print(f"\nTotal overtime hours: {total_overtime:.2f}")
    print(f"Average overtime hours: {average_overtime:.2f}")
    print(
        f"Total overtime expenditure: "
        f"{total_overtime_expenditure:.2f}"
    )

    print(f"Average attendance: {average_attendance:.2f}%")

    print("\nAttendance Categories:")
    print(f"Excellent: {excellent}")
    print(f"Satisfactory: {satisfactory}")
    print(f"Needs improvement: {needs_improvement}")

    print(
        f"\nEmployees with unexplained absences: "
        f"{unexplained_absences}"
    )


# ------------------------------------------------------------
# 17. Display menu
# ------------------------------------------------------------

def display_menu():

    print("\n")
    print("=" * 60)
    print("EMPLOYEE ATTENDANCE AND OVERTIME ANALYSER")
    print("=" * 60)
    print("1. View all valid employee records")
    print("2. Search for an employee")
    print("3. Analyse employee attendance")
    print("4. View employees requiring attendance improvement")
    print("5. Analyse overtime")
    print("6. Compare departments")
    print("7. View invalid records")
    print("8. View organisational summary")
    print("9. Exit")
    print("=" * 60)


# ------------------------------------------------------------
# 18. Main program
# ------------------------------------------------------------

def main():

    # Validate all supplied records
    valid_records, invalid_records = validate_all_records(
        EMPLOYEE_RECORDS
    )

    # Calculate attendance, overtime and payment
    valid_records = prepare_records(valid_records)

    supplied_count = len(EMPLOYEE_RECORDS)

    print("\nEmployee Attendance and Overtime Analyser")
    print("Employee records loaded successfully.")

    while True:

        display_menu()

        choice = input(
            "Enter your selection: "
        ).strip()

        if choice == "1":

            view_valid_records(valid_records)

        elif choice == "2":

            search_employee(valid_records)

        elif choice == "3":

            analyse_attendance(valid_records)

        elif choice == "4":

            view_attendance_improvement(valid_records)

        elif choice == "5":

            analyse_overtime(valid_records)

        elif choice == "6":

            compare_departments(valid_records)

        elif choice == "7":

            view_invalid_records(invalid_records)

        elif choice == "8":

            organisational_summary(
                supplied_count,
                valid_records,
                invalid_records
            )

        elif choice == "9":

            print("\nProgram closed.")
            break

        else:

            print("\nInvalid selection. Please choose 1 to 9.")


# ------------------------------------------------------------
# 19. Run program
# ------------------------------------------------------------

if __name__ == "__main__":
    main()