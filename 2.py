class TrainBookingInterface(TrainBookingSystem):
    def display_welcome_message(self):
        print("Welcome to the Train Ticket Booking System")

    def get_booking_confirmation(self):
        confirmation = input("Do you want to book a ticket? (yes/no): ")
        return confirmation.lower()

    def get_full_name(self):
        return input("Enter your full name: ")

    def get_age(self):
        while True:
            try:
                age = int(input("Enter your age: "))
                if age > 0:
                    return age
                else:
                    print("Please enter a valid age.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def get_number_of_persons(self):
        while True:
            try:
                number_of_persons = int(input("Enter number of persons: "))
                if number_of_persons > 0:
                    return number_of_persons
                else:
                    print("Please enter a valid number of persons.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def display_train_list(self):
        print("\nAvailable Trains:")
        for train in self.trains:
            print(f"- {train}")

    def get_train_choice(self):
        chosen_train = input("Enter the name of the train you want to book: ")
        if chosen_train in self.trains:
            return chosen_train
        else:
            return None

    def get_train_price(self, chosen_train):
        prices = {
            "Express Line": 600,
            "Rapid Rail": 700,
            "City Connect": 550,
            "Interstate": 800
        }
        return prices.get(chosen_train, 0)

    def check_seat_availability(self, num_persons):
        available_seats = [seat for seat, booked in self.seats.items() if not booked]
        if len(available_seats) >= num_persons:
            return available_seats[:num_persons]
        else:
            return None

    def book_seats(self, seat_numbers):
        for seat in seat_numbers:
            self.seats[seat] = True

    def calculate_total_amount(self, price_per_person, number_of_persons):
        return price_per_person * number_of_persons

    def calculate_discount(self, total_amount):
        return 200 if total_amount >= 2000 else 0

    def display_booking_details(self, full_name, chosen_train, total_amount, discount_amount, net_total, seat_numbers):
        print(f"\nHi {full_name}, you've booked tickets for the '{chosen_train}' train.")
        print(f"Seat Numbers: {', '.join(seat_numbers)}")
        if discount_amount > 0:
            print(f"Your total bill is more than 2000, so you get a discount of 200.")
        print(f"The total amount to pay is {net_total:.2f}")

