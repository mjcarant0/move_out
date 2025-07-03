"""
This module handles user signup functionality for app.
It validates user input using the InputValidator and interacts with the database 
via the DatabaseManager to store user account information securely.
"""

from backend.database_manager import DatabaseManager  # Handles all interactions with the database
from backend.validators import InputValidator         # Used to validate and format all user input
from typing import Dict, Any                  # For precise type hints in return values and args

class SignupHandler:
    """
    Handle user signup functionality.
    """
    
    def __init__(self, db_manager: DatabaseManager = None): 
        self.db_manager = db_manager or DatabaseManager()  # If no database manager is passed, initialize a new one

        self.validator = InputValidator()   # Instantiate input validation utility

    
    def create_user(self, first_name: str, last_name: str, country_code: str, 
                   phone_number: str, pin: str, confirm_pin: str) -> Dict[str, Any]:  
        """
        Handle user sign-up.
        
        Args:
            first_name: User's first name
            last_name: User's last name
            phone_number: Phone number
            pin: 4-digit PIN
            confirm pin: must match PIN
            
        Returns:
            Dict with 'success' (bool) and 'message' (str) keys
        """
        try:
            # Input validation
            if not self.validator.validate_name(first_name):
                return {"success": False, "message": "Invalid first name. Only letters and spaces allowed."}
            
            if not self.validator.validate_name(last_name):
                return {"success": False, "message": "Invalid last name. Only letters and spaces allowed."}
            
            if not self.validator.validate_phone_number(phone_number):
                return {"success": False, "message": "Invalid phone number format."}
            
            if not self.validator.validate_pin(pin):
                return {"success": False, "message": "PIN must be exactly 4 digits."}
            
            if not self.validator.validate_pin(confirm_pin):
                return {"success": False, "message": "Confirm PIN must be exactly 4 digits."}

            if not self.validator.validate_pin_confirmation(pin, confirm_pin):
                return {"success": False, "message": "PIN and Confirm PIN do not match."}

            
            # Clean and format inputs
            first_name = self.validator.format_name(first_name)
            last_name = self.validator.format_name(last_name)
            phone_number = self.validator.clean_phone_number(phone_number)
            
            # Combine country code and phone number for storage
            full_phone_number = "+63" + phone_number
            
            # Check if a user with the same number already exists
            existing_user = self.db_manager.execute_query(
                "SELECT id FROM users WHERE phone_number = ?", 
                (full_phone_number,)
            )
            
            if existing_user:
                return {"success": False, "message": "Phone number already registered."}
            
            # If all checks pass, insert the user and get their ID
            user_id = self.db_manager.get_last_insert_id(
                '''INSERT INTO users (first_name, last_name, country_code, phone_number, pin)
                   VALUES (?, ?, ?, ?, ?)''',
                (first_name, last_name, country_code, full_phone_number, pin)
            )
            
            return {
                "success": True, 
                "message": "Account created successfully!",
                "user_id": user_id
            }
        
       # Catch and report any errors during validation or DB operations
        except Exception as e:
            return {"success": False, "message": f"Error creating account: {str(e)}"}
        