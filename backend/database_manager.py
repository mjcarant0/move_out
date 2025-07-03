"""
This module manages all database operations for the app, including connecting 
to the SQLite database, initializing user tables, handling signup, login, and account updates.
"""

import os
import sqlite3
from typing import Any

class DatabaseManager:
    # Provides methods for interacting with the user database.

    def __init__(self, db_name: str = None):
        # Set path to /move_out/data/user_information.db
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        self.db_name = db_name or os.path.join(data_dir, "user_information.db")
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database and create necessary tables."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                # Users table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        country_code TEXT NOT NULL,
                        phone_number TEXT NOT NULL UNIQUE,
                        pin TEXT NOT NULL
                    )
                ''')

                # Pending bookings
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS pending_bookings (
                        booking_id TEXT PRIMARY KEY,
                        user_phone TEXT NOT NULL,
                        vehicle_id TEXT NOT NULL,
                        vehicle_type TEXT NOT NULL,
                        driver_name TEXT NOT NULL,
                        license_plate TEXT NOT NULL,
                        distance REAL NOT NULL,
                        fare REAL NOT NULL,
                        pickup TEXT NOT NULL,
                        dropoff TEXT NOT NULL,
                        timestamp TEXT NOT NULL
                    )
                ''')

                # Cancelled and completed (same structure, initially empty)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cancelled_bookings AS SELECT * FROM pending_bookings WHERE 0
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS completed_bookings AS SELECT * FROM pending_bookings WHERE 0
                ''')

                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Database initialization failed: {str(e)}")
    
    def get_connection(self):
        """Get a new database connection."""
        return sqlite3.connect(self.db_name)
    
    def execute_query(self, query: str, params: tuple = ()) -> Any:
        """Execute a query and return all results."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Query execution failed: {str(e)}")
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute an update/insert/delete query and return rows affected."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            raise Exception(f"Update execution failed: {str(e)}")
    
    def get_last_insert_id(self, query: str, params: tuple = ()) -> int:
        """Execute an insert query and return the last inserted ID."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception(f"Insert execution failed: {str(e)}")
        
    def add_pending_booking(self, booking: tuple) -> None:
        """
        Add a pending booking (11 fields).
        Format: (booking_id, user_phone, vehicle_id, vehicle_type, driver_name,
                 license_plate, distance, fare, pickup, dropoff, timestamp)
        """
        self.execute_update(
            "INSERT INTO pending_bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            booking,
        )

    def get_bookings(self, table: str, user_phone: str) -> list[sqlite3.Row]:
        """Get all bookings for one user from a specific table."""
        assert table in (
            "pending_bookings",
            "completed_bookings",
            "cancelled_bookings",
        ), "Invalid table name"
        return self.execute_query(
            f"SELECT * FROM {table} WHERE user_phone = ?", (user_phone,)
        )

    def delete_booking(self, table: str, booking_id: str) -> None:
        """Delete a booking by ID from the specified table."""
        self.execute_update(
            f"DELETE FROM {table} WHERE booking_id = ?", (booking_id,)
        )
