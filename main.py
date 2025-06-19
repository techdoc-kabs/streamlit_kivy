from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List
from datetime import datetime

app = FastAPI()

# SQLite setup
def get_db_connection():
    conn = sqlite3.connect("patients.db")
    conn.row_factory = sqlite3.Row
    return conn

# Pydantic model
class Patient(BaseModel):
    name: str
    age: int
    gender: str
    date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize DB table
def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
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

# Routes
@app.get("/patients")
def get_patients():
    conn = get_db_connection()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return [dict(row) for row in patients]

@app.post("/patients")
def add_patient(patient: Patient):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
              (patient.name, patient.age, patient.gender, patient.date))
    conn.commit()
    conn.close()
    return {"message": "Patient added successfully"}




# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import sqlite3
# from typing import List
# from datetime import datetime

# app = FastAPI()

# # # SQLite setup
# # def get_db_connection():
# #     conn = sqlite3.connect("patients.db")
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # # Pydantic model
# # class Patient(BaseModel):
# #     uuid: str
# #     name: str
# #     age: int
# #     gender: str
# #     date: str

# # # Initialize DB table with uuid
# # def init_db():
# #     conn = get_db_connection()
# #     c = conn.cursor()
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS patients (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             uuid TEXT UNIQUE,
# #             name TEXT NOT NULL,
# #             age INTEGER NOT NULL,
# #             gender TEXT NOT NULL,
# #             date TEXT NOT NULL
# #         )
# #     ''')
# #     conn.commit()
# #     conn.close()

# # init_db()

# # # Routes
# # @app.get("/patients")
# # def get_patients():
# #     conn = get_db_connection()
# #     patients = conn.execute("SELECT * FROM patients").fetchall()
# #     conn.close()
# #     return [dict(row) for row in patients]

# # @app.post("/patients")
# # def add_patient(patient: Patient):
# #     conn = get_db_connection()
# #     c = conn.cursor()

# #     # Check if patient already exists (by uuid)
# #     existing = c.execute("SELECT * FROM patients WHERE uuid = ?", (patient.uuid,)).fetchone()
# #     if existing:
# #         conn.close()
# #         return {"message": "Patient already exists"}

# #     c.execute(
# #         "INSERT INTO patients (uuid, name, age, gender, date) VALUES (?, ?, ?, ?, ?)",
# #         (patient.uuid, patient.name, patient.age, patient.gender, patient.date)
# #     )
# #     conn.commit()
# #     conn.close()
# #     return {"message": "Patient added successfully"}


