"""
This module manages all database operations for the app, including connecting 
to the SQLite database, initializing user tables, handling signup, login, and account updates.
"""

import os
import sqlite3  # Enables creating and interacting with the local user database.
from typing import Any  # Used for type hints when return types may vary

class DatabaseManager:
    # Provides methods for interacting with the user database, such as creating tables, 
    # inserting users, validating credentials, and updating account information.

    def __init__(self, db_name: str = None):
        # Set path to /move_out/data/user_information.db
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # move_out/
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        self.db_name = db_name or os.path.join(data_dir, "user_information.db")
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database and create the users table if it doesn't exist."""
        try:
            with sqlite3.connect(self.db_name) as conn:  # Connect to the database (creates the file if it doesn't exist)

                cursor = conn.cursor()  # Used to execute SQL commands
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        country_code TEXT NOT NULL,
                        phone_number TEXT NOT NULL UNIQUE,
                        pin TEXT NOT NULL
                    )
                ''')   # If the table already exists, this won’t recreate it
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

                # CANCELLED BOOKINGS TABLE (same structure, empty)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cancelled_bookings AS SELECT * FROM pending_bookings WHERE 0
                ''')

                # COMPLETED BOOKINGS TABLE (same structure, empty)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS completed_bookings AS SELECT * FROM pending_bookings WHERE 0
                ''')
                conn.commit()  # Saves changes to the database
                    # If something goes wrong with SQLite (like a bad connection), raise a clearer error
       
        # If an issue with sqlite occurs, display an error message.
        except sqlite3.Error as e:
            raise Exception(f"Database initialization failed: {str(e)}")
    
    def get_connection(self):
        """Get a database connection."""
        return sqlite3.connect(self.db_name)
    
    def execute_query(self, query: str, params: tuple = ()) -> Any:
        """Execute a query and returns whatever results the query finds"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params) # Runs the SQL query with provided parameters
                return cursor.fetchall()      # Returns the results as a list of rows
        # If an issue with sqlite occurs, display an error message.
        except sqlite3.Error as e:
            raise Exception(f"Query execution failed: {str(e)}")
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute an update/insert/delete query and return rows affected."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)  # Runs the SQL query with provided parameters
                conn.commit()                  # Saves the change
                return cursor.rowcount         # Returns number of rows affected
        # If an issue with sqlite occurs, display an error message.
        except sqlite3.Error as e:
            raise Exception(f"Update execution failed: {str(e)}")
    
    def get_last_insert_id(self, query: str, params: tuple = ()) -> int:
        """Execute an insert query and return the last inserted ID."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid   # Returns the auto-generated ID of the new row    
        # If an issue with sqlite occurs, display an error message.
        except sqlite3.Error as e:
            raise Exception(f"Insert execution failed: {str(e)}")

