# Employee Attendance & Overtime Analyser

An MSc *Fundamentals of Programming* capstone project. A menu-driven Python program
that validates employee records and analyses attendance, overtime and payments for
an organisation.

## Problem statement

Organisations need to monitor staff attendance and compute overtime pay accurately.
Raw employee data is often inconsistent (mixed employment-type spellings, missing
IDs or departments, impossible values such as negative hours). Processing this data
by hand is slow and error-prone.

This program takes a set of employee records, validates them against a clear set of
rules, separates valid from invalid records, and then produces attendance and
overtime analysis to support management decisions.

## Objectives

- Validate each employee record and clearly report why any record is rejected.
- Standardise inconsistent employment-type values (e.g. `full time` to `Full-time`).
- Calculate attendance percentage, absence days and an attendance category.
- Calculate standard hours, overtime hours and payments (regular, overtime, total).
- Identify best and worst performers for attendance and overtime.
- Compare departments by average attendance and overtime expenditure.
- Produce an organisation-wide summary.

## Project structure

```
project-name/
├── README.md          # This file
├── main.py            # The main program (console application)
├── tests.md           # Manual test cases and expected results
├── docs/
│   └── algorithm.pdf  # Algorithm design / flow documentation
└── .gitignore
```

## Program functions

The core logic in `main.py` is organised into these functions:

| Function | Purpose |
|----------|---------|
| `standardise_employment_type()` | Maps spelling variations to recognised employment types. |
| `validate_record()` | Validates a single record and returns a list of errors. |
| `validate_all_records()` | Splits all records into valid and invalid lists. |
| `calculate_attendance()` | Computes absence days, attendance % and category. |
| `calculate_overtime()` | Computes standard/overtime hours and payments. |
| `prepare_records()` | Adds attendance and overtime results to valid records. |
| `view_valid_records()` | Displays all valid employee records. |
| `search_employee()` | Finds an employee by ID or name. |
| `analyse_attendance()` | Lists attendance and highlights highest/lowest. |
| `view_attendance_improvement()` | Lists employees needing attendance improvement. |
| `analyse_overtime()` | Lists overtime/payments and top earners. |
| `compare_departments()` | Compares departments by attendance and overtime cost. |
| `view_invalid_records()` | Displays rejected records with reasons. |
| `organisational_summary()` | Prints organisation-wide totals and averages. |
| `display_menu()` / `main()` | Menu loop that drives the program. |

## Validation rules

A record is **invalid** if any of the following is true:

- Employee ID is missing.
- Employee name is missing.
- Department is missing.
- Expected days is not greater than zero.
- Present days is negative.
- Leave days is negative.
- Present days plus leave days exceed expected days.
- Hours worked is negative.
- Hourly rate is not greater than zero.
- Employment type is not recognised (not Full-time, Part-time or Contract after standardising).

## Calculation rules

- **Standard hours:** Full-time = 160, Part-time = 80, Contract = 120.
- **Overtime hours** = hours worked minus standard hours (never below zero).
- **Overtime pay** = overtime hours x hourly rate x 1.5.
- **Attendance %** = (present days + leave days) / expected days x 100.
- **Attendance categories:** Excellent (>= 95%), Satisfactory (>= 85%), Needs improvement (< 85%).

## Running instructions

Requires Python 3.9 or later. No external libraries are needed for the console program.

```bash
python main.py
```

Follow the on-screen menu (options 1 to 9) to view records, search, run analyses
or exit.

## Optional: Streamlit interface

A Streamlit app (in the `streamlit/` folder) provides a graphical, browser-based
front end for the same analysis. It is only a UI/UX layer. All the core logic and
rules live in `main.py`. The Streamlit app is optional and not required to run or
assess the project.

To run it locally:

```bash
pip install streamlit pandas
streamlit run streamlit/app.py
```
