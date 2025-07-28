from flask import Flask, jsonify, request
import sqlite3
from models.db import reset_init_db
app = Flask(__name__)
DB = "database.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def setup():
    conn = get_db()
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT,
        timings TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        doctor_id INTEGER,
        patient_id INTEGER,
        FOREIGN KEY (doctor_id) REFERENCES doctors(id)
    )''')

    # Seed sample data (only if missing)
    cursor.execute('INSERT OR IGNORE INTO doctors (id, name, specialization, timings) VALUES (?, ?, ?, ?)', 
                   (1, "Dr. Smith", "Cardiologist", "10am-4pm"))
    cursor.execute('INSERT OR IGNORE INTO doctors (id, name, specialization, timings) VALUES (?, ?, ?, ?)', 
                   (2, "Dr. Jane", "Dermatologist", "12pm-6pm"))

    conn.commit()
    conn.close()

# GET /doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    conn = get_db()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    conn.close()
    return jsonify([dict(row) for row in doctors])

# GET /doctors/:id
@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    conn = get_db()
    doctor = conn.execute('SELECT * FROM doctors WHERE id = ?', (doctor_id,)).fetchone()
    conn.close()
    if doctor:
        return jsonify(dict(doctor))
    return jsonify({"error": "Doctor not found"}), 404

# POST /appointments
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    required = ['date', 'time', 'doctor_id', 'patient_id']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db()
    doctor = conn.execute('SELECT * FROM doctors WHERE id = ?', (data['doctor_id'],)).fetchone()
    if not doctor:
        conn.close()
        return jsonify({"error": "Doctor not found"}), 404

    conn.execute('INSERT INTO appointments (date, time, doctor_id, patient_id) VALUES (?, ?, ?, ?)', 
                 (data['date'], data['time'], data['doctor_id'], data['patient_id']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Appointment booked"}), 201

# GET /appointments?doctor_id= or ?patient_id=
@app.route('/appointments', methods=['GET'])
def get_appointments():
    doctor_id = request.args.get('doctor_id')
    patient_id = request.args.get('patient_id')

    conn = get_db()
    cursor = conn.cursor()

    if doctor_id:
        appointments = cursor.execute('SELECT * FROM appointments WHERE doctor_id = ?', (doctor_id,)).fetchall()
    elif patient_id:
        appointments = cursor.execute('SELECT * FROM appointments WHERE patient_id = ?', (patient_id,)).fetchall()
    else:
        conn.close()
        return jsonify({"error": "Specify doctor_id or patient_id"}), 400

    conn.close()
    return jsonify([dict(row) for row in appointments])

# Run the app

if __name__ == "__main__":
    from models.db import reset_init_db
    reset_init_db()  # Reset the DB before starting the server
    app.run(host="0.0.0.0", port=5001, debug=True)

