class Appointment:
    def __init__(self, patient_name, doctor_name, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.time = time

    def display(self):
        return f"Patient: {self.patient_name}, Doctor: {self.doctor_name}, Time: {self.time}"