import streamlit as st
import sqlite3
from datetime import datetime
import requests
import pandas as pd


# --- DB Setup ---
conn = sqlite3.connect('patients.db', check_same_thread=False)
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

# --- Streamlit UI ---
st.title("📝 Patient Registration")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    submitted = st.form_submit_button("Register")

    if submitted:
        if name and age:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
                      (name, age, gender, now))
            conn.commit()
            st.success("✅ Patient registered successfully!")
        else:
            st.error("Please fill in all fields.")

# --- Display Records ---
if st.checkbox("📄 Show Registered Patients"):
    df = st.data_editor(
        conn.execute("SELECT * FROM patients").fetchall(),
        num_rows="dynamic",
        use_container_width=True,
    )


API_URL = "http://127.0.0.1:8000/patients"  

st.title("Synced Patients")
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.error("Failed to fetch patients")
except Exception as e:
    st.error(f"Error: {str(e)}")
