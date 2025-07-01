import sqlite3
import os 

# Initialization of the database
def get_connection(db_name):
    try:
        # Create a path to the Data directory
        data_dir = os.path.join(os.path.dirname(__file__), "stored_data")
        os.makedirs(data_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Full path to the database file inside the Data folder
        db_path = os.path.join(data_dir, db_name)
        
        return sqlite3.connect(db_path)
    except Exception as e:
        print(f"Error : {e}")
        raise

# Create table for the vehicle database
def vehicle_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS vehicles ( 
    vehicle_id TEXT PRIMARY KEY,
    vehicle_type TEXT,
    license_plate TEXT,
    driver_name TEXT,
    is_available INTEGER,
    capacity INTEGER,
    base_fare REAL,
    cost_per_mile REAL
    )
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def user_log_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users ( 
        user_id TEXT PRIMARY KEY,
        phone_number TEXT UNIQUE,
        last_name TEXT,
        first_name TEXT,
        email TEXT UNIQUE,
    )
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

# Main function wrapper 
def main():
    connection = get_connection("move_out.db")

if __name__ =="__main__":
    main()