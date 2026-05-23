from models.patient import Patient

DATA_FILE = "data/patients.txt"


def save_patient(patient):
    # Bukaanka cusub ayuu ku darayaa file-ka

    with open(DATA_FILE, "a") as file:
        file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.phone},{patient.disease}\n")


def get_all_patients():
    # Dhammaan bukaannada ayuu ka akhrinayaa file-ka

    patients = []

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    patients.append(Patient(data[0], data[1], data[2], data[3], data[4]))

    except FileNotFoundError:
        pass

    return patients


def update_patient(patient_id, new_patient):
    # Bukaanka ID-ga la siiyay ayuu update-gareynayaa

    patients = get_all_patients()
    found = False

    with open(DATA_FILE, "w") as file:
        for patient in patients:
            if patient.patient_id == patient_id:
                file.write(f"{new_patient.patient_id},{new_patient.name},{new_patient.age},{new_patient.phone},{new_patient.disease}\n")
                found = True
            else:
                file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.phone},{patient.disease}\n")

    return found


def delete_patient(patient_id):
    # Bukaanka ID-ga la siiyay ayuu tirtirayaa

    patients = get_all_patients()
    found = False

    with open(DATA_FILE, "w") as file:
        for patient in patients:
            if patient.patient_id == patient_id:
                found = True
                continue

            file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.phone},{patient.disease}\n")

    return found