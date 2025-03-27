import sqlite3

class TrainBookingSystem:
    def __init__(self, db_name='train_booking.db'):
        self.db_name = db_name
        self.db_connection = sqlite3.connect(self.db_name)
        self.trains = ["Express Line", "Rapid Rail", "City Connect", "Interstate"]
        self.seats = {f"S{i}": False for i in range(1, 101)}  # 100 seats available
        self.create_bookings_table()

    def create_bookings_table(self):
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    train_name TEXT NOT NULL,
                    number_of_persons INTEGER NOT NULL,
                    total_amount REAL NOT NULL,
                    discount_amount REAL NOT NULL,
                    net_total REAL NOT NULL,
                    seat_numbers TEXT NOT NULL
                )
            ''')

    def insert_booking(self, full_name, age, train_name, number_of_persons, total_amount, discount_amount, net_total, seat_numbers):
        with self.db_connection:
            self.db_connection.execute('''
                INSERT INTO bookings (full_name, age, train_name, number_of_persons, total_amount, discount_amount, net_total, seat_numbers)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (full_name, age, train_name, number_of_persons, total_amount, discount_amount, net_total, ','.join(seat_numbers)))

    def __del__(self):
        self.db_connection.close()

