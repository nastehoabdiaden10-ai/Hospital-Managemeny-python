from models.patient import Patient
from utils.store import save_patient, get_all_patients, update_patient, delete_patient


def show_menu():
    # Menu-ga system-ka

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Exit")


while True:
    show_menu()

    choice = input("Choose option: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        phone = input("Enter Patient Phone: ")
        disease = input("Enter Disease: ")

        patient = Patient(patient_id, name, age, phone, disease)
        save_patient(patient)

        print("Patient added successfully!")

    elif choice == "2":
        patients = get_all_patients()

        print("\n===== Patients List =====")

        if len(patients) == 0:
            print("No patients found.")
        else:
            for patient in patients:
                print(patient.display())

    elif choice == "3":
        old_id = input("Enter Patient ID to update: ")

        new_id = input("Enter New Patient ID: ")
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        phone = input("Enter New Phone: ")
        disease = input("Enter New Disease: ")

        new_patient = Patient(new_id, name, age, phone, disease)

        if update_patient(old_id, new_patient):
            print("Patient updated successfully!")
        else:
            print("Patient not found!")

    elif choice == "4":
        patient_id = input("Enter Patient ID to delete: ")

        if delete_patient(patient_id):
            print("Patient deleted successfully!")
        else:
            print("Patient not found!")

    elif choice == "5":
        print("System Closed")
        break

    else:
        print("Invalid choice! Try again.")