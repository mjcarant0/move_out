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

# Main function wrapper 
def main():
    connection = get_connection("test.db")

if __name__ =="__main__":
    main()