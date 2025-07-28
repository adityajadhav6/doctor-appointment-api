from flask import Blueprint, request, jsonify
from services.appointment_service import (
    create_appointment,
    get_appointments_by_doctor,
    get_appointments_by_patient,
)

appointment_bp = Blueprint("appointments", __name__)

@appointment_bp.route("/", methods=["POST"])
def book():
    data = request.get_json()
    if not all(k in data for k in ("date", "time", "doctor_id", "patient_id")):
        return jsonify({"error": "Missing fields"}), 400
    return create_appointment(data)

@appointment_bp.route("/", methods=["GET"])
def view():
    doctor_id = request.args.get("doctor_id")
    patient_id = request.args.get("patient_id")

    if doctor_id:
        return jsonify(get_appointments_by_doctor(int(doctor_id)))
    if patient_id:
        return jsonify(get_appointments_by_patient(int(patient_id)))

    return jsonify({"error": "Provide doctor_id or patient_id"}), 400
