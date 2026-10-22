# Patient Appointment No-Show & Wait-Time Pipeline

## Executive Summary
A beginner-friendly mini-ETL (Extract, Transform, Load) pipeline built in Python and SQL to analyze clinical scheduling data. The project processes raw appointment records, calculates patient wait times, loads the data into a SQLite database, and runs foundational SQL queries to analyze appointment volume by department and filter patient no-shows.

## The Problem Solved
Clinics need to track scheduling metrics and patient attendance to improve operational efficiency. Manually reviewing raw scheduling logs is tedious and inefficient. This pipeline automates date calculation, database loading, and basic SQL reporting to help operations teams monitor departmental appointment distribution and attendance patterns.

## Tech Stack & Skills Demonstrated
* **Programming & Data Manipulation:** Python, Pandas (Datetime handling, feature engineering)
* **Database & Querying:** SQLite (`sqlite3`), SQL Foundational Queries (`GROUP BY`, `COUNT`, `WHERE`)
* **Core Analytics Skills:** Data Cleansing, Feature Engineering, Relational Database Management

## Pipeline Architecture & Workflow
1. **Extraction:** Ingests raw clinical appointment data (`raw_appointments.csv`).
2. **Transformation (Pandas):** 
   * Converts raw date strings into Python datetime objects.
   * Calculates `Wait_Days` (the time gap between when an appointment was scheduled and the actual visit date).
3. **Loading:** Saves the cleaned records into a local SQLite database (`clinical_ops.db`) under the `appointments` table.
4. **SQL Reporting:** Executes straightforward SQL queries to count total appointments by department and filter for patient no-shows.

## How to Run

To clean the data, load the database, and run the SQL reports, execute the following commands in your terminal:

```bash
py clean_and_load.py
py query_noshows.py