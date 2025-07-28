from flask import Blueprint, jsonify
from services.doctor_service import list_doctors, get_doctor_by_id

doctor_bp = Blueprint("doctors", __name__)

@doctor_bp.route("/", methods=["GET"])
def get_doctors():
    return jsonify(list_doctors())

@doctor_bp.route("/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):
    doctor = get_doctor_by_id(doctor_id)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404
    return jsonify(doctor)
