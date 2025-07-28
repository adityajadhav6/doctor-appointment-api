from models.data_store import appointments
from services.doctor_service import get_doctor_by_id

def create_appointment(data):
    doctor = get_doctor_by_id(data["doctor_id"])
    if not doctor:
        return {"error": "Doctor not found"}, 404

    new_appointment = {
        "id": len(appointments) + 1,
        "date": data["date"],
        "time": data["time"],
        "doctor_id": data["doctor_id"],
        "patient_id": data["patient_id"]
    }
    appointments.append(new_appointment)
    return new_appointment, 201

def get_appointments_by_doctor(doctor_id):
    return [a for a in appointments if a["doctor_id"] == doctor_id]

def get_appointments_by_patient(patient_id):
    return [a for a in appointments if a["patient_id"] == patient_id]