def main():
    booking_system = TrainBookingInterface()
    booking_system.display_welcome_message()
    confirmation = booking_system.get_booking_confirmation()

    if confirmation == "yes":
        booking_system.display_train_list()
        chosen_train = booking_system.get_train_choice()
        
        if chosen_train:
            price_per_person = booking_system.get_train_price(chosen_train)
            full_name = booking_system.get_full_name()
            age = booking_system.get_age()
            number_of_persons = booking_system.get_number_of_persons()
            available_seats = booking_system.check_seat_availability(number_of_persons)
            
            if available_seats:
                booking_system.book_seats(available_seats)
                total_amount = booking_system.calculate_total_amount(price_per_person, number_of_persons)
                discount_amount = booking_system.calculate_discount(total_amount)
                net_total = total_amount - discount_amount
                booking_system.display_booking_details(full_name, chosen_train, total_amount, discount_amount, net_total, available_seats)
                
                # Store booking in the database
                booking_system.insert_booking(full_name, age, chosen_train, number_of_persons, total_amount, discount_amount, net_total, available_seats)
            else:
                print("Sorry, not enough seats are available. Please try a different train or reduce the number of persons.")
        else:
            print("Sorry, the train you entered is not available. Please try again.")
    else:
        print("No booking made. Thank you!")

if __name__ == "__main__":
    main()
