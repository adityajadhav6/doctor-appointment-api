from models.data_store import doctors

def list_doctors():
    return doctors

def get_doctor_by_id(doc_id):
    return next((doc for doc in doctors if doc["id"] == doc_id), None)
