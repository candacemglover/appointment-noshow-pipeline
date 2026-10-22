import os
import sqlite3
import pandas as pd

#Locate file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data', 'raw_appointments.csv')
db_path = os.path.join(script_dir, 'data', 'clinical_ops.db')

#Ingest raw CSV data
df = pd.read_csv(csv_path)

#Convert date columns to datetime objects
df['Scheduled_Date'] = pd.to_datetime(df['Scheduled_Date'])
df['Appointment_Date'] = pd.to_datetime(df['Appointment_Date'])

#Feature Engineering: Calculate Wait Days
df['Wait_Days'] = (df['Appointment_Date'] - df['Scheduled_Date']).dt.days

#Convert dates back to string format for SQLite compatibility
df['Scheduled_Date'] = df['Scheduled_Date'].dt.strftime('%Y-%m-%d')
df['Appointment_Date'] = df['Appointment_Date'].dt.strftime('%Y-%m-%d')

print("-" * 50)
print(f"Data Cleaning Complete! Processed {len(df)} appointment records.")
print("-" * 50)
print(df[['Appointment_ID', 'Department', 'Wait_Days', 'No_Show']])
print("-" * 50)

#Load into SQLite Database Table
conn = sqlite3.connect(db_path)
df.to_sql('appointments', conn, if_exists='replace', index=False)
conn.close()

print(f"Database successfully created at: {db_path}")