# ============================================================
# Employee Attendance and Overtime Analyser - Streamlit App
# MSc Fundamentals of Programming - Capstone Project
# ============================================================

import pandas as pd
import streamlit as st

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Employee Attendance & Overtime Analyser",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ------------------------------------------------------------
# Theme / styling (Blue & White)
# ------------------------------------------------------------

st.markdown(
    """
    <style>
        /* App background */
        .stApp {
            background-color: #f4f8ff;
        }

        /* Main title banner */
        .app-banner {
            background: linear-gradient(135deg, #0b5ed7 0%, #1e88e5 100%);
            padding: 28px 32px;
            border-radius: 14px;
            color: #ffffff;
            margin-bottom: 24px;
            box-shadow: 0 6px 18px rgba(11, 94, 215, 0.25);
        }
        .app-banner h1 {
            color: #ffffff;
            margin: 0;
            font-size: 30px;
            font-weight: 700;
        }
        .app-banner p {
            color: #e3f0ff;
            margin: 6px 0 0 0;
            font-size: 15px;
        }

        /* Section headers */
        .section-header {
            background-color: #0b5ed7;
            color: #ffffff;
            padding: 10px 18px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: 600;
            margin: 8px 0 18px 0;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #d6e4ff;
            border-left: 5px solid #0b5ed7;
            border-radius: 10px;
            padding: 16px 18px;
            box-shadow: 0 2px 8px rgba(11, 94, 215, 0.08);
        }
        div[data-testid="stMetricLabel"] {
            color: #0b5ed7;
            font-weight: 600;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0b5ed7;
        }
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* Dataframe container tweak */
        .stDataFrame {
            border-radius: 10px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# 1. Employee data
# ------------------------------------------------------------

EMPLOYEE_RECORDS = [
    {"employee_id": "E001", "employee_name": "Jane Wanjiku", "department": "Finance", "employment_type": "Full-time", "days_expected": 22, "days_present": 20, "leave_days": 2, "hours_worked": 176, "hourly_rate": 850},
    {"employee_id": "E002", "employee_name": "Brian Otieno", "department": "IT", "employment_type": "full time", "days_expected": 22, "days_present": 19, "leave_days": 1, "hours_worked": 185, "hourly_rate": 920},
    {"employee_id": "E003", "employee_name": "Amina Hassan", "department": "Human Resources", "employment_type": "Part-time", "days_expected": 20, "days_present": 17, "leave_days": 2, "hours_worked": 88, "hourly_rate": 700},
    {"employee_id": "E004", "employee_name": "Peter Mwangi", "department": "Operations", "employment_type": "Contract", "days_expected": 22, "days_present": 18, "leave_days": 0, "hours_worked": 146, "hourly_rate": 780},
    {"employee_id": "E005", "employee_name": "Lucy Njeri", "department": "Sales", "employment_type": "FULL-TIME", "days_expected": 22, "days_present": 21, "leave_days": 1, "hours_worked": 168, "hourly_rate": 810},
    {"employee_id": "E006", "employee_name": "David Kiptoo", "department": "Operations", "employment_type": "Full-time", "days_expected": 22, "days_present": 16, "leave_days": 1, "hours_worked": 172, "hourly_rate": 760},
    {"employee_id": "E007", "employee_name": "Faith Atieno", "department": "Finance", "employment_type": "part time", "days_expected": 20, "days_present": 19, "leave_days": 1, "hours_worked": 92, "hourly_rate": 680},
    {"employee_id": "E008", "employee_name": "Samuel Kariuki", "department": "IT", "employment_type": "Contract", "days_expected": 22, "days_present": 22, "leave_days": 0, "hours_worked": 132, "hourly_rate": 880},
    {"employee_id": "E009", "employee_name": "Mercy Chebet", "department": "Sales", "employment_type": "Full-time", "days_expected": 22, "days_present": 18, "leave_days": 2, "hours_worked": 158, "hourly_rate": 790},
    {"employee_id": "E010", "employee_name": "John Kamau", "department": "Human Resources", "employment_type": "Full-time", "days_expected": 22, "days_present": 20, "leave_days": 1, "hours_worked": 164, "hourly_rate": 820},
    {"employee_id": "E011", "employee_name": "Rose Achieng", "department": "Operations", "employment_type": "Contract", "days_expected": 22, "days_present": 21, "leave_days": 1, "hours_worked": 151, "hourly_rate": 740},
    {"employee_id": "E012", "employee_name": "Kevin Mutua", "department": "IT", "employment_type": "Part-time", "days_expected": 20, "days_present": 15, "leave_days": 1, "hours_worked": 78, "hourly_rate": 710},
    {"employee_id": "E013", "employee_name": "Grace Wambui", "department": "Finance", "employment_type": "Full-time", "days_expected": 22, "days_present": 23, "leave_days": 0, "hours_worked": 170, "hourly_rate": 860},
    {"employee_id": "E014", "employee_name": "Allan Musyoka", "department": "Sales", "employment_type": "Intern", "days_expected": 22, "days_present": 19, "leave_days": 1, "hours_worked": 162, "hourly_rate": 620},
    {"employee_id": "E015", "employee_name": "Esther Jepkoech", "department": "Operations", "employment_type": "Full-time", "days_expected": 22, "days_present": 18, "leave_days": 2, "hours_worked": -5, "hourly_rate": 770},
    {"employee_id": None, "employee_name": "Mohamed Noor", "department": "IT", "employment_type": "Contract", "days_expected": 22, "days_present": 20, "leave_days": 1, "hours_worked": 128, "hourly_rate": 900},
    {"employee_id": "E017", "employee_name": "Irene Muthoni", "department": None, "employment_type": "Full-time", "days_expected": 22, "days_present": 21, "leave_days": 0, "hours_worked": 166, "hourly_rate": 830},
    {"employee_id": "E018", "employee_name": "Collins Ouma", "department": "Sales", "employment_type": "Part-time", "days_expected": 20, "days_present": 17, "leave_days": 1, "hours_worked": 86, "hourly_rate": 0},
    {"employee_id": "E019", "employee_name": "Diana Wafula", "department": "Finance", "employment_type": "Contract", "days_expected": 22, "days_present": 17, "leave_days": 3, "hours_worked": 124, "hourly_rate": 795},
    {"employee_id": "E020", "employee_name": "Joseph Maina", "department": "IT", "employment_type": "Full-time", "days_expected": 22, "days_present": 21, "leave_days": 1, "hours_worked": 194, "hourly_rate": 950},
]


# ------------------------------------------------------------
# 2. Constants
# ------------------------------------------------------------

STANDARD_HOURS = {
    "Full-time": 160,
    "Part-time": 80,
    "Contract": 120,
}

OVERTIME_MULTIPLIER = 1.5


# ------------------------------------------------------------
# 3. Employment type standardisation
# ------------------------------------------------------------

def standardise_employment_type(employment_type):
    """Standardise obvious variations in employment type."""
    if not isinstance(employment_type, str):
        return None

    value = employment_type.strip().lower()

    mappings = {
        "full-time": "Full-time",
        "full time": "Full-time",
        "part-time": "Part-time",
        "part time": "Part-time",
        "contract": "Contract",
    }

    return mappings.get(value)


# ------------------------------------------------------------
# 4. Validate one employee record
# ------------------------------------------------------------

def validate_record(record):
    """Validate an individual employee record. Returns a list of errors."""
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
        errors.append("Present days plus leave days cannot exceed expected days.")

    if hours_worked is None or hours_worked < 0:
        errors.append("Hours worked cannot be negative.")

    if hourly_rate is None or hourly_rate <= 0:
        errors.append("Hourly rate must be greater than zero.")

    standardised_type = standardise_employment_type(record.get("employment_type"))

    if standardised_type is None:
        errors.append("Employment type is not recognised.")

    return errors


# ------------------------------------------------------------
# 5. Validate all records
# ------------------------------------------------------------

def validate_all_records(records):
    """Validate all supplied employee records."""
    valid_records = []
    invalid_records = []

    for record in records:
        errors = validate_record(record)

        if errors:
            invalid_records.append({"record": record, "reasons": errors})
        else:
            valid_record = record.copy()
            valid_record["employment_type"] = standardise_employment_type(
                record["employment_type"]
            )
            valid_records.append(valid_record)

    return valid_records, invalid_records


# ------------------------------------------------------------
# 6. Attendance calculations
# ------------------------------------------------------------

def calculate_attendance(record):
    """Calculate absence days, attendance percentage and category."""
    expected = record["days_expected"]
    present = record["days_present"]
    leave = record["leave_days"]

    absence_days = expected - present - leave
    attendance_percentage = ((present + leave) / expected) * 100

    if attendance_percentage >= 95:
        category = "Excellent"
    elif attendance_percentage >= 85:
        category = "Satisfactory"
    else:
        category = "Needs improvement"

    return {
        "absence_days": absence_days,
        "attendance_percentage": attendance_percentage,
        "attendance_category": category,
    }


# ------------------------------------------------------------
# 7. Overtime and payment calculations
# ------------------------------------------------------------

def calculate_overtime(record):
    """Calculate standard/overtime hours and payments."""
    employment_type = record["employment_type"]
    standard_hours = STANDARD_HOURS[employment_type]

    hours_worked = record["hours_worked"]
    hourly_rate = record["hourly_rate"]

    overtime_hours = hours_worked - standard_hours
    if overtime_hours < 0:
        overtime_hours = 0

    regular_hours = min(hours_worked, standard_hours)
    regular_payment = regular_hours * hourly_rate
    overtime_payment = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_payment = regular_payment + overtime_payment

    return {
        "standard_hours": standard_hours,
        "overtime_hours": overtime_hours,
        "regular_payment": regular_payment,
        "overtime_payment": overtime_payment,
        "total_payment": total_payment,
    }


# ------------------------------------------------------------
# 8. Prepare calculated employee records
# ------------------------------------------------------------

def prepare_records(valid_records):
    """Add attendance, overtime and payment calculations to records."""
    prepared_records = []

    for record in valid_records:
        employee = record.copy()
        employee.update(calculate_attendance(employee))
        employee.update(calculate_overtime(employee))
        prepared_records.append(employee)

    return prepared_records


# ------------------------------------------------------------
# Helpers for the UI
# ------------------------------------------------------------

@st.cache_data
def load_data():
    valid_records, invalid_records = validate_all_records(EMPLOYEE_RECORDS)
    valid_records = prepare_records(valid_records)
    return valid_records, invalid_records


def records_to_df(records):
    return pd.DataFrame(records)


def category_badge(category):
    colors = {
        "Excellent": "#198754",
        "Satisfactory": "#0d6efd",
        "Needs improvement": "#dc3545",
    }
    color = colors.get(category, "#6c757d")
    return (
        f"<span style='background-color:{color};color:#fff;"
        f"padding:3px 10px;border-radius:12px;font-size:13px;'>{category}</span>"
    )


def section(title):
    st.markdown(f"<div class='section-header'>{title}</div>", unsafe_allow_html=True)


# ------------------------------------------------------------
# Load data once
# ------------------------------------------------------------

valid_records, invalid_records = load_data()
supplied_count = len(EMPLOYEE_RECORDS)


# ------------------------------------------------------------
# Banner
# ------------------------------------------------------------

st.markdown(
    """
    <div class="app-banner">
        <h1>📊 Employee Attendance & Overtime Analyser</h1>
        <p>MSc Fundamentals of Programming - Capstone Project</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# Sidebar navigation
# ------------------------------------------------------------

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Choose a view",
    [
        "🏠 Overview",
        "👥 Valid Records",
        "🔍 Search Employee",
        "📈 Attendance Analysis",
        "⚠️ Attendance Improvement",
        "⏱️ Overtime Analysis",
        "🏢 Department Comparison",
        "🚫 Invalid Records",
        "📋 Organisational Summary",
    ],
)

st.sidebar.markdown("---")
st.sidebar.metric("Supplied records", supplied_count)
st.sidebar.metric("Valid records", len(valid_records))
st.sidebar.metric("Invalid records", len(invalid_records))


# ============================================================
# VIEWS
# ============================================================

# ------------------------------------------------------------
# Overview
# ------------------------------------------------------------

if menu == "🏠 Overview":
    section("Overview")

    df = records_to_df(valid_records)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Valid Employees", len(valid_records))
    col2.metric("Avg Attendance", f"{df['attendance_percentage'].mean():.2f}%")
    col3.metric("Total Overtime Hrs", f"{df['overtime_hours'].sum():.0f}")
    col4.metric("Total Overtime Pay", f"{df['overtime_payment'].sum():,.0f}")

    st.markdown("### Attendance by Employee")
    chart_df = df.set_index("employee_name")[["attendance_percentage"]]
    st.bar_chart(chart_df, color="#0b5ed7")

    st.markdown("### Overtime Payment by Employee")
    ot_df = df.set_index("employee_name")[["overtime_payment"]]
    st.bar_chart(ot_df, color="#1e88e5")


# ------------------------------------------------------------
# Valid Records
# ------------------------------------------------------------

elif menu == "👥 Valid Records":
    section("Valid Employee Records")

    if not valid_records:
        st.info("No valid employee records available.")
    else:
        df = records_to_df(valid_records)

        display_df = df[
            [
                "employee_id", "employee_name", "department", "employment_type",
                "days_expected", "days_present", "leave_days", "absence_days",
                "attendance_percentage", "attendance_category",
                "hours_worked", "standard_hours", "overtime_hours",
                "hourly_rate", "regular_payment", "overtime_payment", "total_payment",
            ]
        ].rename(
            columns={
                "employee_id": "ID",
                "employee_name": "Name",
                "department": "Department",
                "employment_type": "Type",
                "days_expected": "Expected",
                "days_present": "Present",
                "leave_days": "Leave",
                "absence_days": "Absence",
                "attendance_percentage": "Attendance %",
                "attendance_category": "Category",
                "hours_worked": "Hours",
                "standard_hours": "Std Hrs",
                "overtime_hours": "OT Hrs",
                "hourly_rate": "Rate",
                "regular_payment": "Regular Pay",
                "overtime_payment": "OT Pay",
                "total_payment": "Total Pay",
            }
        )

        st.dataframe(
            display_df.style.format(
                {
                    "Attendance %": "{:.2f}",
                    "OT Hrs": "{:.2f}",
                    "Rate": "{:,.2f}",
                    "Regular Pay": "{:,.2f}",
                    "OT Pay": "{:,.2f}",
                    "Total Pay": "{:,.2f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )


# ------------------------------------------------------------
# Search Employee
# ------------------------------------------------------------

elif menu == "🔍 Search Employee":
    section("Search for an Employee")

    search_value = st.text_input("Enter employee ID or name").strip().lower()

    if search_value:
        found = None
        for employee in valid_records:
            if (
                search_value == str(employee["employee_id"]).lower()
                or search_value == str(employee["employee_name"]).lower()
            ):
                found = employee
                break

        if found:
            st.success(f"Employee found: {found['employee_name']} ({found['employee_id']})")

            c1, c2, c3 = st.columns(3)
            c1.metric("Attendance", f"{found['attendance_percentage']:.2f}%")
            c2.metric("Overtime Hours", f"{found['overtime_hours']:.2f}")
            c3.metric("Total Payment", f"{found['total_payment']:,.2f}")

            st.markdown(
                f"**Department:** {found['department']} &nbsp;|&nbsp; "
                f"**Employment Type:** {found['employment_type']} &nbsp;|&nbsp; "
                f"**Category:** {category_badge(found['attendance_category'])}",
                unsafe_allow_html=True,
            )
            st.markdown(f"**Overtime Payment:** {found['overtime_payment']:,.2f}")
        else:
            st.error("Employee not found.")
    else:
        st.info("Type an employee ID (e.g. E020) or full name (e.g. Joseph Maina).")


# ------------------------------------------------------------
# Attendance Analysis
# ------------------------------------------------------------

elif menu == "📈 Attendance Analysis":
    section("Employee Attendance Analysis")

    if not valid_records:
        st.info("No valid records available.")
    else:
        df = records_to_df(valid_records)

        table = df[["employee_id", "employee_name", "attendance_percentage", "attendance_category"]].rename(
            columns={
                "employee_id": "ID",
                "employee_name": "Name",
                "attendance_percentage": "Attendance %",
                "attendance_category": "Category",
            }
        )
        st.dataframe(
            table.style.format({"Attendance %": "{:.2f}"}),
            use_container_width=True,
            hide_index=True,
        )

        highest = df["attendance_percentage"].max()
        lowest = df["attendance_percentage"].min()

        highest_emps = df[df["attendance_percentage"] == highest]["employee_name"].tolist()
        lowest_emps = df[df["attendance_percentage"] == lowest]["employee_name"].tolist()

        c1, c2 = st.columns(2)
        with c1:
            st.success(f"**Highest Attendance: {highest:.2f}%**\n\n{', '.join(highest_emps)}")
        with c2:
            st.error(f"**Lowest Attendance: {lowest:.2f}%**\n\n{', '.join(lowest_emps)}")


# ------------------------------------------------------------
# Attendance Improvement
# ------------------------------------------------------------

elif menu == "⚠️ Attendance Improvement":
    section("Employees Requiring Attendance Improvement")

    employees = [
        e for e in valid_records if e["attendance_category"] == "Needs improvement"
    ]

    if not employees:
        st.success("No employees require attendance improvement.")
    else:
        df = records_to_df(employees)
        table = df[["employee_id", "employee_name", "attendance_percentage", "absence_days"]].rename(
            columns={
                "employee_id": "ID",
                "employee_name": "Name",
                "attendance_percentage": "Attendance %",
                "absence_days": "Absence Days",
            }
        )
        st.dataframe(
            table.style.format({"Attendance %": "{:.2f}"}),
            use_container_width=True,
            hide_index=True,
        )


# ------------------------------------------------------------
# Overtime Analysis
# ------------------------------------------------------------

elif menu == "⏱️ Overtime Analysis":
    section("Overtime and Payment Analysis")

    if not valid_records:
        st.info("No valid records available.")
    else:
        df = records_to_df(valid_records)

        table = df[
            ["employee_id", "employee_name", "overtime_hours", "overtime_payment", "total_payment"]
        ].rename(
            columns={
                "employee_id": "ID",
                "employee_name": "Name",
                "overtime_hours": "OT Hours",
                "overtime_payment": "OT Payment",
                "total_payment": "Total Payment",
            }
        )
        st.dataframe(
            table.style.format(
                {"OT Hours": "{:.2f}", "OT Payment": "{:,.2f}", "Total Payment": "{:,.2f}"}
            ),
            use_container_width=True,
            hide_index=True,
        )

        max_ot = df["overtime_hours"].max()
        max_ot_pay = df["overtime_payment"].max()
        max_total = df["total_payment"].max()

        c1, c2, c3 = st.columns(3)
        c1.metric(
            "Most Overtime Hours",
            f"{max_ot:.2f}",
            ", ".join(df[df["overtime_hours"] == max_ot]["employee_name"].tolist()),
        )
        c2.metric(
            "Highest OT Payment",
            f"{max_ot_pay:,.0f}",
            ", ".join(df[df["overtime_payment"] == max_ot_pay]["employee_name"].tolist()),
        )
        c3.metric(
            "Highest Total Payment",
            f"{max_total:,.0f}",
            ", ".join(df[df["total_payment"] == max_total]["employee_name"].tolist()),
        )


# ------------------------------------------------------------
# Department Comparison
# ------------------------------------------------------------

elif menu == "🏢 Department Comparison":
    section("Department Comparison")

    if not valid_records:
        st.info("No valid records available.")
    else:
        df = records_to_df(valid_records)

        grouped = df.groupby("department").agg(
            average_attendance=("attendance_percentage", "mean"),
            overtime_expenditure=("overtime_payment", "sum"),
            employees=("employee_id", "count"),
        ).reset_index()

        table = grouped.rename(
            columns={
                "department": "Department",
                "average_attendance": "Avg Attendance %",
                "overtime_expenditure": "OT Expenditure",
                "employees": "Employees",
            }
        )
        st.dataframe(
            table.style.format({"Avg Attendance %": "{:.2f}", "OT Expenditure": "{:,.2f}"}),
            use_container_width=True,
            hide_index=True,
        )

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Average Attendance by Department**")
            st.bar_chart(grouped.set_index("department")[["average_attendance"]], color="#0b5ed7")
        with c2:
            st.markdown("**Overtime Expenditure by Department**")
            st.bar_chart(grouped.set_index("department")[["overtime_expenditure"]], color="#1e88e5")

        highest = grouped["overtime_expenditure"].max()
        highest_depts = grouped[grouped["overtime_expenditure"] == highest]["department"].tolist()
        st.warning(
            f"**Highest Overtime Expenditure:** {', '.join(highest_depts)} ({highest:,.2f})"
        )


# ------------------------------------------------------------
# Invalid Records
# ------------------------------------------------------------

elif menu == "🚫 Invalid Records":
    section("Invalid Employee Records")

    if not invalid_records:
        st.success("No invalid records found.")
    else:
        for item in invalid_records:
            record = item["record"]
            with st.expander(
                f"{record.get('employee_id')} - {record.get('employee_name')} "
                f"({record.get('department')})"
            ):
                st.markdown("**Reason(s):**")
                for reason in item["reasons"]:
                    st.markdown(f"- {reason}")


# ------------------------------------------------------------
# Organisational Summary
# ------------------------------------------------------------

elif menu == "📋 Organisational Summary":
    section("Organisational Summary")

    if not valid_records:
        st.info("No valid records available.")
    else:
        df = records_to_df(valid_records)

        total_overtime = df["overtime_hours"].sum()
        average_overtime = df["overtime_hours"].mean()
        total_overtime_expenditure = df["overtime_payment"].sum()
        average_attendance = df["attendance_percentage"].mean()

        excellent = (df["attendance_category"] == "Excellent").sum()
        satisfactory = (df["attendance_category"] == "Satisfactory").sum()
        needs_improvement = (df["attendance_category"] == "Needs improvement").sum()
        unexplained_absences = (df["absence_days"] > 0).sum()

        c1, c2, c3 = st.columns(3)
        c1.metric("Supplied records", supplied_count)
        c2.metric("Valid records", len(valid_records))
        c3.metric("Invalid records", len(invalid_records))

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Overtime Hrs", f"{total_overtime:.2f}")
        c2.metric("Avg Overtime Hrs", f"{average_overtime:.2f}")
        c3.metric("Total OT Expenditure", f"{total_overtime_expenditure:,.2f}")
        c4.metric("Avg Attendance", f"{average_attendance:.2f}%")

        st.markdown("### Attendance Categories")
        cat_df = pd.DataFrame(
            {
                "Category": ["Excellent", "Satisfactory", "Needs improvement"],
                "Count": [int(excellent), int(satisfactory), int(needs_improvement)],
            }
        ).set_index("Category")
        st.bar_chart(cat_df, color="#0b5ed7")

        st.info(f"**Employees with unexplained absences:** {int(unexplained_absences)}")


# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit • Blue & White theme")
