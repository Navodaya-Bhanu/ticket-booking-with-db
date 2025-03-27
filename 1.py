def main():
    # Initialize database and create table
    create_bookings_table()
    
    trains = ["Express Line", "Rapid Rail", "City Connect", "Interstate"]
    seats = {f"S{i}": False for i in range(1, 101)}  # 100 seats available
    
    display_welcome_message()
    confirmation = get_booking_confirmation()

    if confirmation == "yes":
        display_train_list(trains)
        chosen_train = get_train_choice(trains)
        
        if chosen_train:
            price_per_person = get_train_price(chosen_train)
            full_name = get_full_name()
            age = get_age()
            number_of_persons = get_number_of_persons()
            available_seats = check_seat_availability(seats, number_of_persons)
            
            if available_seats:
                book_seats(seats, available_seats)
                total_amount = calculate_total_amount(price_per_person, number_of_persons)
                discount_amount = calculate_discount(total_amount)
                net_total = total_amount - discount_amount
                display_booking_details(full_name, chosen_train, total_amount, discount_amount, net_total, available_seats)
                
                # Store booking in the database
                insert_booking(full_name, age, chosen_train, number_of_persons, total_amount, discount_amount, net_total, available_seats)
            else:
                print("Sorry, not enough seats are available. Please try a different train or reduce the number of persons.")
        else:
            print("Sorry, the train you entered is not available. Please try again.")
    else:
        print("No booking made. Thank you!")

# Establish database connection
db_connection = sqlite3.connect('train_booking.db')

# Run the main function
main()

# Close the database connection when done
db_connection.close()
