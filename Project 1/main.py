import json
import os
from datetime import datetime
from abc import abstractmethod, ABC

PATIENT_FILE = "Project 1/patients.json"
DOCTOR_FILE = "Project 1/doctors.json"
APPOINTMENT_FILE = "Project 1/appointments.json"
BILL_FILE = "Project 1/bills.json"


class JSONstorage:

    @staticmethod
    def load_data(filename):
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_data(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

class Person(ABC):
    def __init__(self, name, age, gender, contact):
        self._name = name
        self._age = age
        self._gender = gender
        self._contact = contact

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def contact(self):
        return self._contact

    @abstractmethod
    def display_info(self):
        pass


class Patient(Person):
    def __init__(self, patient_id, name, age, gender, contact, disease, address=""):
        super().__init__(name, age, gender, contact)
        self.patient_id = patient_id
        self.disease = disease
        self.address = address
        self.admit_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def display_info(self):
        print(f"[Patient ID: {self.patient_id}] Name: {self.name} | Age: {self.age} "
              f"Gender: {self._gender} | Contact: {self._contact} | Disease: {self.disease}")

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            'name': self.name,
            'age': self.age,
            'gender': self._gender,
            'contact': self.contact,
            'disease': self.disease,
            'address': self.address,
            'admit_date': self.admit_date
        }

class Doctor(Person):
    def __init__(self, d_id, name, age, gender, contact, specialization, fee):
        super().__init__(name, age, gender, contact)
        self.doctor_id = d_id
        self.specialization = specialization
        self.fee = fee

    def display_info(self):
        print(f"[Doctor ID: {self.doctor_id}] Dr. {self.name} | Specialization {self.specialization} | "
              f"Consultation Fee: Rs.{self.fee} | Contact: {self.contact}")
                      

    def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            'name': self.name,
            'age': self.age,
            'gender': self._gender,
            'contact': self.contact,
            'specialization': self.specialization,
            'fee': self.fee
        }

class Appointment:
    def __init__(self, ap_id, p_id, d_id, date, status = 'Scheduled'):
        self.appointment_id = ap_id
        self.patient_id = p_id
        self.doctor_id = d_id
        self.date = date
        self.status = status

    def to_dict(self):
        return self.__dict__

    def display_info(self):
        print(f"[Appointment ID: {self.appointment_id}] Patient: {self.patient_id} | "
              f"Doctor: {self.doctor_id} | Date: {self.date} | Status: {self.status}")

class Bill:
    GST_RATE = 0.18

    def __init__(self, bill_id, patient_id, doctor_id, consultation_fee, medicine_charges):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.consultation_fee = consultation_fee
        self.medicine_charges = medicine_charges
        self.gst_amount = self.calculate_gst()
        self.total_amount = self.calculate_total()
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def calculate_gst(self):
        subtotal = self.consultation_fee + self.medicine_charges
        return round(subtotal * Bill.GST_RATE, 2)

    def calculate_total(self):
        subtotal = self.consultation_fee + self.medicine_charges
        return round(subtotal + self.gst_amount, 2)

    def display_bill(self):
        print('----HOSPITAL BILL----')
        print(f"Bill ID: {self.bill_id}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Consultation Fee: {self.consultation_fee}")
        print(f"Medicine Charges: {self.medicine_charges}")
        print(f"GST (18%): {self.gst_amount}")
        print()
        print(f"Total Amount: {self.total_amount}")
        print()

    def to_dict(self):
        return self.__dict__
              
class HospitalManagementSystem:
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'admin123'

    def __init__(self):
        self.patients = JSONstorage.load_data(PATIENT_FILE)
        self.doctors = JSONstorage.load_data(DOCTOR_FILE)
        self.appointments = JSONstorage.load_data(APPOINTMENT_FILE)
        self.bills = JSONstorage.load_data(BILL_FILE)

    def admin_login(self):
        print("\n---- ADMIN LOGIN ----")
        username = input('Enter Username: ')
        password = input('Enter Password: ')

        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            print("\nLogin Successful! Welcome Admin.\n")
            return True
        else:
            print("\nInvalid Username or Password\n")
            return False

    def genrate_id(self, records, prefix):
        number = len(records) + 1
        return f"{prefix}{number:03d}"

    def add_patient(self):
        print("\n---- ADD NEW PATIENT ----")
        name = input('Enter Patient Name: ')
        age = input('Enter Age: ')
        gender = input('Enter Gender (Male/Female/Other): ')
        contact = input('Enter Contact Number: ')
        disease = input('Enter Disease/Problem: ')
        address = input('Enter Address: ')

        if not name.strip() or not contact.strip():
            print("\nError: Name and Contact cannot be empty!\n")


        try:
            age = int(age)
        except ValueError:
            print("\nError: Age must be a number!\n")
            return

        patient_id = self.genrate_id(self.patients, "P")
        new_patient = Patient(patient_id, name, age, gender, contact, disease, address)

        self.patients.append(new_patient.to_dict())
        JSONstorage.save_data(PATIENT_FILE, self.patients)

        print(f"\nPatient Added Successfully! Patient ID: {patient_id}\n")

    def search_patient(self):
        print("\n---- SEARCH PATIENT ----")
        keyword = input('Enter Patient ID or Name to search: ').strip().lower()

        results = [p for p in self.patients
                   if keyword in p["patient_id"].lower() or keyword in p["name"].lower()]

        if results:
            print(f"\n{len(results)} result(s) found:\n")
            for p in results:
                print(f"ID: {p['patient_id']} | Name: {p['name']} | Age: {p['age']} | "
                      f"Gender: {p['gender']} | Contact: {p['contact']} | Disease: {p['disease']}")
        else:
            print("\nNo matching patient found!\n")

    def update_patient(self):
        print("\n---- UPDATE PATIENT ----")
        patient_id = input('Enter Patient ID to update: ').strip()

        for p in self.patients:
            if p['patient_id'] == patient_id:
                print("Current Details:", p)
                print("\nLeave field blank to keep current value.")

                new_name = input(f"New Name [{p['name']}]: ").strip()
                new_contact = input(f"New Contact [{p['contact']}]: ").strip()
                new_disease = input(f"New Disease [{p['disease']}]: ").strip()

                if new_name:
                    p['name'] = new_name
                if new_contact:
                    p['contact'] = new_contact
                if new_disease:
                    p['disease'] = new_disease

                JSONstorage.save_data(PATIENT_FILE, self.patients)
                print("\nPatient Updated Successfully\n")

        print("\nPatient Not Found\n")

    def delete_patient(self):
        print("\n---- DELETE PATIENT ----")
        patient_id = input('Enter Patient ID to delete: ').strip()
        
        for p in self.patients:
            if p['patient_id'] == patient_id:
                confirm = input(f"Are you sure you want to delte {p['name']}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    self.patients.remove(p)
                    JSONstorage.save_data(PATIENT_FILE, self.patients)
                    print("\nPatient Deleted Successfully!\n")
                else:
                    print("\nDeletion Cancelled.\n")
                return
        print("\nPatient Not Found!\n")

    def display_all_patients(self):
        print("\n---- ALL PATIENTS ----")
        if not self.patients:
            print('No patients found in the system.\n')
            return

        for p in self.patients:
            print(f"[Patient ID: {self.patient_id}] Name: {self.name} | Age: {self.age} "
                  f"Gender: {self._gender} | Contact: {self._contact} | Disease: {self.disease}") 
        print(f"\nTotal Patients: {len(self.patients)}\n")

    def add_doctor(self):
        print("\n---- ADD NEW DOCTOR ----")
        name = input('Enter Doctor Name: ')
        age = input('Enter Age: ')
        gender = input('Enter Gender (Male/Female/Other): ')
        contact = input('Enter Contact Number: ')
        specialization = input('Enter Specialization (e.g. Cardiologist): ')
        fee = input('Enter Consultation Fee: ')

        if not name.strip() or not contact.strip():
            print("\nError: Name and Contact cannot be empty!\n")
            return

        try:
            age = int(age)
            fee = float(fee)
        except ValueError:
            print("\nError: Age & Fee must be a numbers!\n")
            return

        doctor_id = self.genrate_id(self.doctors, "D")
        new_doctor = Patient(doctor_id, name, age, gender, contact, specialization, fee)
        
        self.doctors.append(new_doctor.to_dict())
        JSONstorage.save_data(DOCTOR_FILE, self.doctors)
        
        print(f"\nDoctor Added Successfully! Doctor ID: {doctor_id}\n")

    def search_doctor(self):
        print("\n---- SEARCH DOCTOR ----")
        keyword = input('Enter Doctor ID or Name to search: ').strip().lower()
        
        results = [d for d in self.doctors if
                   keyword in d['doctor_id'].lower() or
                   keyword in d['name'].lower() or
                   keyword in d['specialization'].lower()]
        
        if results:
            print(f"\n{len(results)} result(s) found:\n")
            for d in results:
                print(f"ID: {d['doctor_id']} | Dr. {d['name']} | Specialization: {d['specialization']} | "
                  f"Fee: Rs.{d['fee']} | Contact: {d['contact']}")
            else:
                print("\nNo matching doctor found!\n")

    def update_doctor(self):
        print("\n---- UPDATE DOCTOR ----")
        doctor_id = input('Enter Doctor ID to update: ').strip()


        for d in self.doctors:
            if d['doctor_id'] == doctor_id:
                print("Current Details:", d)
                print("\nLeave field blank to keep current value.")


                new_contact = input(f"New Contact [{d['contact']}]: ").strip()
                new_fee = input(f"New Fee [{d['fees']}]: ").strip()


                if new_contact:
                    d['contact'] = new_contact
                if new_fee:
                    try:
                        d['fee'] = float(new_fee)
                    except ValueError:
                        print('\nInvalid Fee, keeping old value\n')
                JSONstorage.save_data(DOCTOR_FILE, self.doctors)

                print("\nDoctor Updated Successfully\n")
                return

        print("\nDoctor Not Found\n")

    def display_all_doctors(self):
        print("\n---- ALL DOCTORS ----")
        if not self.doctors:
            print('No doctors found in the system.\n')
            return

        for d in self.doctors:
            print(f"[ID: {d['doctor_id']}] Dr. {d['name']} | Specialization: {d['specialization']} "
                  f"Fee: {d['fee']} | Contact: {d['contact']}") 
        print(f"\nTotal Doctors: {len(self.doctors)}\n")

    def book_appointment(self):
        print('\n---- BOOK APPOINTMENT ----')
        patient_id = input('Enter Patient ID: ').strip()
        doctor_id = input('Enter Doctor ID: ').strip()

        patient_exist = any(p['patient_id'] == patient_id for p in self.patients)
        doctor_exist = any(d['doctor_id'] == doctor_id for d in self.doctors)

        if not patient_exist:
            print('\nPatient ID not found\n')
            return
        if not doctor_exist:
            print('\nDoctor ID not found\n')
            return

        date = input('Enter Appointment Date (YYYY-MM-DD): ').strip()
        appointment_id = self.genrate_id(self.appointments, "A")
        new_appointment = Appointment(appointment_id, patient_id, doctor_id, date)
        self.appointments.append(new_appointment.to_dict())
        JSONstorage.save_data(APPOINTMENT_FILE, self.appointments)

        print(f'\nAppointment Booked Successfully! Appointment ID: {appointment_id}\n')

    def cancel_appointment(self):
        print('\n---- CANCEL APPOINTMENT ----')
        appointment_id = input('Enter Appointment ID to cancel: ').strip()

        for a in self.appointments:
            if a['appointment_id'] == appointment_id:
                if a['status'] == 'Cancelled':
                    print('\nThis appointment is already cancelled')
                    return
                a['status'] = 'Cancelled'
                JSONstorage.save_data(APPOINTMENT_FILE, self.appointments)
                print('\nAppointment Cancelled Successfully!\n')
                return
            print('\nAppointment not found\n')


    def generate_bill(self):
        print('\n---- GENERATE BILL ----')
        patient_id = input('Enter Patient ID: ').strip()
        doctor_id = input('Enter Doctor ID: ').strip()

        patient = next((p for p in self.patients if p['patient_id'] == patient_id), None)
        doctor = next((d for d in self.doctors if d['doctor_id'] == doctor_id), None)

        if not patient:
            print('\nPatient not found\n')
            return
        if not doctor:
            print('\nDoctor not found\n')
            return

        consultation_fee = doctor['fee']
        try:
            medicine_charges = float(input('Enter medicine charges: '))
        except ValueError:
            print('\nError: Medicine charges must be a number\n')
            return

        bill_id = self.genrate_id(self.bills, 'B')
        new_bill = Bill(bill_id, patient_id, doctor_id, consultation_fee, medicine_charges)
        self.bills.append(new_bill.to_dict())
        JSONstorage.save_data(BILL_FILE, self.bills)
        new_bill.display_bill()


    def show_reports(self):
        print('\n---- HOSPITAL REPORTS ----')
        total_patients = len(self.patients)
        total_doctors = len(self.doctors)
        total_revenue = sum(bill['total_amount'] for bill in self.bills)

        print(f'Total Patients: {total_patients}')
        print(f'Total Doctors: {total_doctors}')
        print(f'Total Revenue: {total_revenue}')

    def patient_menu(self):
        while True:
            print('\n---- PATIENT MANAGEMENT ----')
            print('1. Add Patient')
            print('2. Search Patient')
            print('3. Update Patient')
            print('4. Delete Patient')
            print('5. Display All Patients')
            print('6. Back to Main Menu')

            choice = input('Enter your choice: ').strip()

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.search_patient()
            elif choice == '3':
                self.update_patient()
            elif choice == '4':
                self.delete_patient()
            elif choice == '5':
                self.display_all_patients()
            elif choice == '6':
                break
            else:
                print('\nInvalid choice! Please try again.\n')

    def doctor_menu(self):
        while True:
            print('\n---- DOCTOR MANAGEMENT ----')
            print('1. Add Doctor')
            print('2. Search Doctor')
            print('3. Update Doctor')
            print('4. Display All Doctors')
            print('5. Back to Main Menu')

            choice = input('Enter your choice: ').strip()

            if choice == '1':
                self.add_doctor()
            elif choice == '2':
                self.search_doctor()
            elif choice == '3':
                self.update_doctor()
            elif choice == '4':
                self.display_all_doctors()
            elif choice == '5':
                break
            else:
                print('\nInvalid choice! Please try again.\n')

    def appointment_menu(self):
        while True:
            print('\n---- APPOINTMENT MANAGEMENT ----')
            print('1. Book Appointment')
            print('2. Cancel Appointment')
            print('3. Back to Main Menu')

            choice = input('Enter your choice: ').strip()

            if choice == '1':
                self.book_appointment()
            elif choice == '2':
                self.cancel_appointment()
            elif choice == '3':
                break
            else:
                print('\nInvalid choice! Please try again.\n')

    def main_menu(self):
            while True:
                print('\n---- HOSPITAL MANAGEMENT SYSTEM ----')
                print('1. Patient Management')
                print('2. Doctor Management')
                print('3. Appointment Management')
                print('4. Generate Bill')
                print('5. Reports')
                print('5. Exit')
                print()

                choice = input('Enter your choice: ').strip()

                if choice == '1':
                    self.patient_menu()
                elif choice == '2':
                    self.doctor_menu()
                elif choice == '3':
                    self.appointment_menu()
                elif choice == '4':
                    self.generate_bill()
                elif choice == '5':
                    self.show_reports()
                elif choice == '6':
                    print('Thank you for using Hospital Management System.')
                else:
                    print('\nInvalid choice! Please try again.\n')

    def run(self):
        print()
        print("    WELCOME TO CITY CARE HOSPITAL MANAGEMENT SYSTEM")
        print()

        if self.admin_login():
            self.main_menu()
        else:
            print('\nAccess Denied. Exiting program.\n')


if __name__ == '__main__':
    system = HospitalManagementSystem()
    system.run()