# import streamlit as st
# import sqlite3
# from datetime import datetime
# import requests
# import pandas as pd
# API_URL = "https://streamlit-kivy.onrender.com/patients" 

# # --- DB Setup ---
# conn = sqlite3.connect('patients.db', check_same_thread=False)
# c = conn.cursor()

# c.execute('''
#     CREATE TABLE IF NOT EXISTS patients (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         gender TEXT NOT NULL,
#         date TEXT NOT NULL

#     )
# ''')
# conn.commit()

# # --- Streamlit UI ---
# st.title("📝 Patient Registration")

# with st.form("registration_form"):
#     name = st.text_input("Full Name")
#     age = st.number_input("Age", min_value=0)
#     gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#     submitted = st.form_submit_button("Register")

#     if submitted:
#         if name and age:
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Save locally
#             c.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
#                       (name, age, gender, now))
#             conn.commit()
    
#             # Also sync to FastAPI
#             payload = {
#                 "name": name,
#                 "age": age,
#                 "gender": gender,
#                 "date": now
#             }
#             try:
#                 response = requests.post(API_URL, json=payload)
#                 if response.status_code == 200:
#                     st.success("✅ Registered and synced to server!")
#                 else:
#                     st.warning(f"Registered locally but failed to sync. Status code: {response.status_code}")
#             except Exception as e:
#                 st.warning(f"Registered locally but sync failed: {str(e)}")
#         else:
#             st.error("Please fill in all fields.")


# # --- Display Records ---
# if st.checkbox("📄 Show Registered Patients"):
#     df = st.data_editor(
#         conn.execute("SELECT * FROM patients").fetchall(),
#         num_rows="dynamic",
#         use_container_width=True,
#     )



# st.title("🧾 Synced Patients from Central API")
# try:
#     response = requests.get(API_URL)
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             df = pd.DataFrame(data)
#             st.dataframe(df)
#         else:
#             st.info("No patients found on the central API.")
#     else:
#         st.error(f"Failed to fetch patients: {response.status_code}")
# except Exception as e:
#     st.error(f"Error: {str(e)}")
import streamlit as st
import sqlite3
from datetime import datetime
import requests
import pandas as pd

# --- API Endpoint ---
API_URL = "https://streamlit-kivy.onrender.com/patients"

# --- Setup local DB ---
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

# --- Auto PUSH: Sync unsynced local records to FastAPI ---
def push_local_to_api():
    unsynced = c.execute("SELECT name, age, gender, date FROM patients").fetchall()
    synced_ids = set()

    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            remote_data = response.json()
            synced_ids = {(p["name"], p["date"]) for p in remote_data}
    except:
        pass  # If API fails, just skip

    new_syncs = 0
    for row in unsynced:
        key = (row[0], row[3])  # (name, date)
        if key not in synced_ids:
            payload = {
                "name": row[0],
                "age": row[1],
                "gender": row[2],
                "date": row[3]
            }
            try:
                r = requests.post(API_URL, json=payload)
                if r.status_code == 200:
                    new_syncs += 1
            except:
                pass
    return new_syncs

# --- Auto PULL: Sync missing API records to local DB ---
def pull_api_to_local():
    pulled = 0
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            central_data = response.json()
            local_records = c.execute("SELECT name, date FROM patients").fetchall()
            local_set = {(row[0], row[1]) for row in local_records}

            for patient in central_data:
                key = (patient["name"], patient["date"])
                if key not in local_set:
                    c.execute("INSERT INTO patients (name, age, gender, date) VALUES (?, ?, ?, ?)",
                              (patient["name"], patient["age"], patient["gender"], patient["date"]))
                    conn.commit()
                    pulled += 1
    except:
        pass
    return pulled

# --- Run sync automatically ---
with st.spinner("🔄 Syncing with central server..."):
    pushed = push_local_to_api()
    pulled = pull_api_to_local()
    st.success(f"✅ Synced: {pushed} pushed to server, {pulled} pulled into local")

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
            st.success("✅ Registered locally — will sync shortly.")
        else:
            st.error("Please fill in all fields.")

# --- Display Local Records ---
if st.checkbox("📄 Show Local Registered Patients"):
    df_local = pd.read_sql_query("SELECT * FROM patients", conn)
    st.dataframe(df_local)

# --- Display Remote (API) Records ---
st.subheader("🧾 Synced Patients from Central API")
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        remote_data = response.json()
        if remote_data:
            df_remote = pd.DataFrame(remote_data)
            st.dataframe(df_remote)
        else:
            st.info("No patients on central API.")
    else:
        st.error("Failed to load central API records.")
except Exception as e:
    st.error(f"❌ API error: {e}")
