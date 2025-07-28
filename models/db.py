import sqlite3
import os

DB_NAME = 'database.db'

def reset_init_db():
    # Delete existing database file
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create doctors table
    cursor.execute('''
        CREATE TABLE doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT,
            timings TEXT
        )
    ''')

    # Create appointments table
    cursor.execute('''
        CREATE TABLE appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time TEXT,
            doctor_id INTEGER,
            patient_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
        )
    ''')

    # Seed fresh data
    cursor.execute('INSERT INTO doctors (name, specialization, timings) VALUES (?, ?, ?)', 
                   ("Dr. Smith", "Cardiologist", "10am-4pm"))
    cursor.execute('INSERT INTO doctors (name, specialization, timings) VALUES (?, ?, ?)', 
                   ("Dr. Jane", "Dermatologist", "12pm-6pm"))
    cursor.execute('INSERT INTO doctors (name, specialization, timings) VALUES (?, ?, ?)',
                   ("Dr. Bharath", "Child Specalist", "10:30am-6pm"))

    conn.commit()
    conn.close()
    print("✔️ Database reset and seeded fresh.")
