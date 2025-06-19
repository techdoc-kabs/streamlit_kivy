from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# ✅ No UUID here
class Patient(BaseModel):
    name: str
    age: int
    gender: str
    date: str

def get_db_connection():
    conn = sqlite3.connect("patients.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.get("/patients")
def get_patients():
    conn = get_db_connection()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return [dict(row) for row in patients]

@app.post("/patients")
def add_patient(patient: Patient):
    conn = get_db_connection()
    conn.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
                 (patient.name, patient.age, patient.gender, patient.date))
    conn.commit()
    conn.close()
    return {"message": "Patient added successfully"}




