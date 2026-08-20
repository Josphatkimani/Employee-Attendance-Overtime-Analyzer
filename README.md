# Employee Attendance & Overtime Analyser

An interactive Streamlit web application that validates employee records and analyses
attendance, overtime and payments for an organisation.

Built as an MSc *Fundamentals of Programming* capstone project. The app converts a
console-based Python analyser into a clean, browser-based dashboard with a blue and
white theme.

## Features

- **Overview dashboard** with key metrics and attendance / overtime charts.
- **Valid records** shown in a sortable, formatted table.
- **Employee search** by ID (e.g. `E020`) or full name (e.g. `Joseph Maina`).
- **Attendance analysis** with highest and lowest performers.
- **Attendance improvement** list for employees below the satisfactory threshold.
- **Overtime analysis** highlighting the top overtime and payment earners.
- **Department comparison** with average attendance and overtime expenditure charts.
- **Invalid records** with the specific reason each record failed validation.
- **Organisational summary** of totals, averages and attendance categories.

## Business rules

- **Employment types** are standardised (e.g. `full time`, `FULL-TIME` all map to `Full-time`).
- **Standard hours:** Full-time = 160, Part-time = 80, Contract = 120.
- **Overtime** is paid at 1.5x the hourly rate for hours worked beyond standard hours.
- **Attendance %** = (days present + leave days) / expected days x 100.
- **Attendance categories:** Excellent (>= 95%), Satisfactory (>= 85%), Needs improvement (< 85%).
- A record is **invalid** if it is missing an ID, name or department, has non-positive
  expected days or hourly rate, has negative present days, leave days or hours worked,
  has present + leave days exceeding expected days, or has an unrecognised employment type.

## Project structure

```
EmployeeAttendanceAnalyzer/
├── app.py                 # Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Blue & white theme settings
└── README.md
```

## Run locally

Requires Python 3.9 or later.

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app → Deploy a public app from GitHub**.
4. Select the repository, set the branch to `main` and the main file path to `app.py`.
5. Click **Deploy**. The app installs the dependencies and launches at a shareable URL.

Pushing new commits to the repository automatically redeploys the app.

## Tech stack

- [Streamlit](https://streamlit.io) - web app framework
- [pandas](https://pandas.pydata.org) - data handling and aggregation
