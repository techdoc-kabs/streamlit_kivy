
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3
from datetime import datetime
import requests

API_URL = "https://streamlit-kivy.onrender.com"  # your FastAPI URL
DB = "offline_patients.db"

# Setup local DB
def create_local_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            date TEXT NOT NULL,
            synced INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

class RegistrationForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.name = TextInput(hint_text="Full Name")
        self.age = TextInput(hint_text="Age", input_filter='int')
        self.gender = TextInput(hint_text="Gender")

        self.add_widget(Label(text="Patient Registration (Offline)"))
        self.add_widget(self.name)
        self.add_widget(self.age)
        self.add_widget(self.gender)

        self.submit_btn = Button(text="Register Offline")
        self.submit_btn.bind(on_press=self.save_patient)
        self.add_widget(self.submit_btn)

        self.sync_btn = Button(text="🔄 Sync with Server")
        self.sync_btn.bind(on_press=self.sync_data)
        self.add_widget(self.sync_btn)

        self.status = Label()
        self.add_widget(self.status)

        create_local_db()

    def save_patient(self, instance):
        name = self.name.text
        age = self.age.text
        gender = self.gender.text
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if name and age and gender:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("INSERT INTO patients (name, age, gender, date, synced) VALUES (?, ?, ?, ?, 0)",
                      (name, int(age), gender, date))
            conn.commit()
            conn.close()
            self.status.text = "✅ Saved locally!"
            self.name.text = self.age.text = self.gender.text = ""
        else:
            self.status.text = "❌ Fill all fields!"

    def sync_data(self, instance):
        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            unsynced = c.execute("SELECT * FROM patients WHERE synced = 0").fetchall()

            if not unsynced:
                self.status.text = "✅ No unsynced data."
                return

            success_count = 0
            for row in unsynced:
                payload = {
                    "name": row[1],
                    "age": row[2],
                    "gender": row[3],
                    "date": row[4]
                }
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    c.execute("UPDATE patients SET synced = 1 WHERE id = ?", (row[0],))
                    success_count += 1

            conn.commit()
            conn.close()
            self.status.text = f"✅ Synced {success_count} records."
        except Exception as e:
            self.status.text = f"❌ Sync failed: {str(e)}"

class OfflineApp(App):
    def build(self):
        return RegistrationForm()

if __name__ == "__main__":
    OfflineApp().run()
