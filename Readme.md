# Doctor-Patient Appointment API

A simple RESTful API built with Flask and Docker to manage doctor listings and patient appointment bookings.

## 🩺 Features

- List all doctors
- View individual doctor details
- Book appointments with doctor ID and patient ID
- View appointments by doctor or patient

## 📦 Technologies Used

- Python 3
- Flask
- SQLite
- Docker

## 🚀 Setup & Run (Without Docker)

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
2. **Install Dependencies**
    pip install -r requirements.txt
3. **Run App**
    python3 app.py
4. **Visit:http://127.0.0.1:5001**

| Method | Endpoint                      | Description                     |
| ------ | ----------------------------- | ------------------------------- |
| GET    | `/doctors`                    | List all doctors                |
| GET    | `/doctors/<id>`               | Get doctor details by ID        |
| POST   | `/appointments`               | Book an appointment             |
| GET    | `/appointments?doctor_id=1`   | View appointments for a doctor  |
| GET    | `/appointments?patient_id=99` | View appointments for a patient |
