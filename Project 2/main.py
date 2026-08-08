import os, json
import random, string   # for PNR

TRAIN_FILE = 'Project 2/trains.json'
BOOKING_FILE = 'Project 2/bookings.json'

class Train:
    def __init__(self, train_number, train_name, source, destination, departure_time, arrival_time, total_seats, available_seats=None):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = available_seats if available_seats is not None else total_seats

    def display_info(self):
        print(f"Train Number: {self.train_number}")
        print(f"Train Name: {self.train_name}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

    def to_dict(self):
        return {
            'train_number': self.train_number,
            'train_name': self.train_name,
            'source': self.source,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'total_seats': self.total_seats,
            'available_seats': self.available_seats
        }

    def has_available_seats(self):
        return self.available_seats > 0


class Passenger:
    def __init__(self, name, age, gender, mobile):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'mobile': self.mobile
        }

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Mobile: {self.mobile}")


def get_valid_name():
    while True:
        name = input('Enter passenger name: ').strip()
        if name == '':
            print('Name cannot be empty. Please try again.')
            continue
        if not all(char.isalpha() or char.isspace() for char in name):
            print('Name should only contain letters and spaces.')
            continue
        return name

def get_valid_age():
    while True:
        age_input = input('Enter passenger age: ')
        try:
            age = int(age_input)
        except ValueError:
            print('Age must be a number. Please try again.')
            continue
        if age <= 0 or age > 120:
            print('Please enter a realistic age between 1 and 120.')
            continue
        return age

def get_valid_gender():
    while True:
        gender = input('Enter Gender M/F/O: ').strip().upper()
        if gender not in ('M', 'F', 'O'):
            print('Please enter M for Male, F for Female, or O for Other.')
            continue
        return gender

def get_valid_mobile():
    while True:
        mobile = input('Enter 10-digit mobile number: ').strip()
        if len(mobile) != 10 or not mobile.isdigit():
            print('Mobile number must be exactly 10 digits.')
            continue
        return mobile

class ReservationSystem:
    def __init__(self):
        self.trains = {}
        self.bookings = {}
        self.load_trains()
        self.load_bookings()

    def create_default_trains(self):
        default_trains = [
            Train('12302', 'Rajdhani Express', 'Delhi', 'Mumbai', '16:00', '8:00', 100),
            Train('12951', 'Shatabdi Express', 'Delhi', 'Chandigarh', '07:30', '11:00', 100),
            Train('12259', 'Duronto Express', 'Mumbai', 'Kolkata', '22:00', '16:00', 100),
            Train('12925', 'Tamil Nadu Express', 'Delhi', 'Chennai', '22:30', '7:00', 100),
            Train('12621', 'Paschim Express', 'Amritsar', 'Mumbai', '12:15', '20:00', 100),
        ]
        self.trains = {train.train_number: train for train in default_trains}
        self.save_trains()


    def load_trains(self):
        if not os.path.exists(TRAIN_FILE):
            self.create_default_trains()
            return

        try:
            with open(TRAIN_FILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print('Warning: trains.json was corrupted. Recreating default trains.')
            self.create_default_trains()
            return

        self.trains = {}

        for train_number, info in data.items():
            self.trains[train_number] = Train(
                info['train_number'],
                info['train_name'],
                info['source'],
                info['destination'],
                info['departure_time'],
                info['arrival_time'],
                info['total_seats'],
                info['available_seats']
            )

    def save_trains(self):
        data = {number: train.to_dict() for number, train in self.trains.items()}
        with open(TRAIN_FILE, 'w') as file:
            json.dump(data, file, indent=4)

    def load_bookings(self):
        if not os.path.exists(BOOKING_FILE):
            self.bookings = {}
            return

        try:
            with open(BOOKING_FILE, 'r') as file:
                self.bookings = json.load(file)
        except json.JSONDecodeError:
            print('Warning: bookings.json war corrupted. Starting with empty bookings.')
            self.bookings = {}

    def save_bookings(self):
        with open(BOOKING_FILE, 'w') as file:
            json.dump(self.bookings, file, indent=4)


    def generate_pnr(self):
        while True:
            pnr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if pnr not in self.bookings:
                return pnr

    def generate_seat_number(self, train):
        booked_seats = [
            booking['seat_number'] for booking in self.bookings.values()
            if booking['train_number'] == train.train_number and booking['status'] == 'Confirmed'
        ]
        seat_number = train.total_seats - train.available_seats + 1
        while seat_number in booked_seats:
            seat_number += 1
        return seat_number

    def book_tickets(self):
        print('BOOK TICKET')
        self.show_all_trains()

        train_number = input('Enter train number to book: ').strip()

        if train_number not in self.trains:
            print('Invalid Train Number. Please try again.')
            return 

        train = self.trains[train_number]

        if not train.has_available_seats():
            print('Sorry, No seats available in this train.')
            return

        name = get_valid_name()
        age = get_valid_age()
        gender = get_valid_gender()
        mobile = get_valid_mobile()

        passenger = Passenger(name, age, gender, mobile)
        pnr = self.generate_pnr()
        seat_number = self.generate_seat_number(train)

        booking = {
            'pnr': pnr,
            'passenger': passenger.to_dict(),
            'train_number': train.train_number,
            'train_name': train.train_name,
            'seat_number': seat_number,
            'status': 'Confirmed'
        }

        self.bookings[pnr] = booking
        train.available_seats -= 1

        self.save_bookings()
        self.save_trains()

        print('\nTicket Booked Successfully!')
        print(f"Your PNR Number is: {pnr}")
        print(f"Seat Number: {seat_number}")
        print('Please note down your pnr for future reference.')


    def cancel_ticket(self):
        print('CANCEL TICKET')
        pnr = input('Enter PNT Number to cancel: ').strip().upper()

        if pnr not in self.bookings:
            print('No booking found with this PNR.')
            return

        booking = self.bookings[pnr]

        if booking['status'] == 'Cancelled':
            print('This ticket is already cancelled.')
            return

        confirm = input(f"Cancel ticket for {booking['passenger']['name']}? (Y/N): ").strip().upper()
        if confirm != 'Y':
            print('Cancellation aborted')
            return

        booking['status'] = 'Cancelled'

        train_number = booking['train_number']
        if train_number in self.trains:
            self.trains[train_number].available_seats += 1

        self.save_trains()
        self.save_bookings()

        print('Ticket cancelled successfully.')


    def search_ticket(self):
        print('SEARCH TICKET')
        pnr = input('Enter PNT Number to search: ').strip().upper()

        if pnr not in self.bookings:
            print('No booking found with this PNR.')
            return

        booking = self.bookings[pnr]
        passenger = booking['passenger']

        print(f"PNR: {booking['pnr']}")
        print(f"Passenger Name: {passenger['name']}")
        print(f"Age: {passenger['age']}")
        print(f"Gender: {passenger['gender']}")
        print(f"Mobile: {passenger['mobile']}")
        print(f"Train Number: {booking['train_number']}")
        print(f"Train Name: {booking['train_name']}")
        print(f"Status: {booking['status']}")

    def display_all_bookings(self):
        print('ALL BOOKINGS')
        if not self.bookings:
            print('No bookings found yet.')
            return

        confirmed = 0
        cancelled = 0

        for pnr, booking in self.bookings.items():
            passenger = booking['passenger']
            print(f"PNR: {booking['pnr']}")
            print(f"Passenger Name: {passenger['name']}")
            print(f"Train Number: {booking['train_number']}")
            print(f"Train Number: {booking['train_number']}")
            print(f"Status: {booking['status']}")

            if booking['status'] == 'Confirmed':
                confirmed += 1
            else:
                cancelled += 1

        print(f'Total bookings: {len(self.bookings)} | Confirmed: {confirmed} | Cancelled: {cancelled}')

    def show_all_trains(self):
        print('TRAIN LIST')
        for train in self.trains.values():
            train.display_info()

    def show_available_seats(self):
        print('AVAILABLE SEATS')
        train_number= input('Enter train number: ')

        if train_number not in self.trains:
            print('Invalid train number.')
            return

        train = self.trains[train_number]
        percentage = (train.available_seats / train.total_seats) * 100

        print(f"{train.train_name} ({train.train_number})")
        print(f"Available Seats: {train.available_seats} out of {train.total_seats}")
        print(f'Occupancy: {100 - percentage:.1f}% full')

    def main_menu(self):
        while True:
            print('RAILWAY RESERVATION SYSTEM')
            print('1. Book ticket')
            print('2. Cancel ticket')
            print('3. Search ticket by PNR')
            print('4. Display All Bookings')
            print('5. Train Details')
            print('6. Available Seats')
            print('7. Exit')

            choice = input('Enter your choice (1-7): ').strip()

            if choice == '1':
                self.book_tickets()
            elif choice == '2':
                self.cancel_ticket()
            elif choice == '3':
                self.search_ticket()
            elif choice == '4':
                self.display_all_bookings()
            elif choice == '5':
                self.show_all_trains()
            elif choice == '6':
                self.show_available_seats()
            elif choice == '7':
                print('Thank you for using Railway Reservation System.')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 7.')

            input('\nPress Enter to Continue')

if __name__ == "__main__":
    system = ReservationSystem()
    system.main_menu()