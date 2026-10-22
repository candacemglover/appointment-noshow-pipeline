import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'data', 'clinical_ops.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 60)
print("SQL QUERY 1: Total Appointments by Department")
print("=" * 60)

#Query 1: Basic grouping and counting
query1 = """
    SELECT Department, COUNT(Appointment_ID) AS Total_Appointments
    FROM appointments
    GROUP BY Department;
"""

cursor.execute(query1)
for row in cursor.fetchall():
    dept, total = row
    dept_str = dept if dept is not None else "Unspecified"
    print(f"Department: {dept_str:<15} | Total Appointments: {total}")

print("\n" + "=" * 60)
print("SQL QUERY 2: Filtering for No-Shows Only")
print("=" * 60)

#Query 2: Basic filtering with WHERE
query2 = """
    SELECT Appointment_ID, Patient_ID, Department, Wait_Days
    FROM appointments
    WHERE No_Show = 'Yes';
"""

cursor.execute(query2)
for row in cursor.fetchall():
    appt_id, patient_id, dept, wait = row
    print(f"Appt ID: {appt_id} | Patient: {patient_id} | Dept: {dept} | Wait Days: {wait}")

print("=" * 60)
conn.close()