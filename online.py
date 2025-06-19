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
            
            # Save locally
            c.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
                      (name, age, gender, now))
            conn.commit()
    
            # Also sync to FastAPI
            payload = {
                "name": name,
                "age": age,
                "gender": gender,
                "date": now
            }
            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    st.success("✅ Registered and synced to server!")
                else:
                    st.warning(f"Registered locally but failed to sync. Status code: {response.status_code}")
            except Exception as e:
                st.warning(f"Registered locally but sync failed: {str(e)}")
        else:
            st.error("Please fill in all fields.")


# --- Display Records ---
if st.checkbox("📄 Show Registered Patients"):
    df = st.data_editor(
        conn.execute("SELECT * FROM patients").fetchall(),
        num_rows="dynamic",
        use_container_width=True,
    )


API_URL = "https://streamlit-kivy.onrender.com/patients"  # ✅ Correct endpoint

st.title("🧾 Synced Patients from Central API")
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("No patients found on the central API.")
    else:
        st.error(f"Failed to fetch patients: {response.status_code}")
except Exception as e:
    st.error(f"Error: {str(e)}")
