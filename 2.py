def create_bookings_table():
    cursor = db_connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER,
            chosen_train TEXT NOT NULL,
            number_of_persons INTEGER,
            total_amount REAL,
            discount_amount REAL,
            net_total REAL,
            seat_numbers TEXT
        )
    ''')
    db_connection.commit()

def insert_booking(full_name, age, chosen_train, number_of_persons, total_amount, discount_amount, net_total, seat_numbers):
    cursor = db_connection.cursor()
    cursor.execute('''
        INSERT INTO bookings (full_name, age, chosen_train, number_of_persons, total_amount, discount_amount, net_total, seat_numbers)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (full_name, age, chosen_train, number_of_persons, total_amount, discount_amount, net_total, ','.join(seat_numbers)))
    db_connection.commit()
