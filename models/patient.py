class Patient:
    # Class-kan wuxuu matalaa xogta bukaanka

    def __init__(self, patient_id, name, age, phone, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone
        self.disease = disease

    def display(self):
        # Qaybtan waxay soo celinaysaa xogta bukaanka
        return f"{self.patient_id} | {self.name} | {self.age} | {self.phone} | {self.disease}"