"""
This module handles user login/authentication functionality.
It validates inputs and checks user credentials using InputValidator and DatabaseManager.
"""

from backend.database_manager import DatabaseManager  # Manages database operations like querying user data
from backend.validators import InputValidator         # Used to validate and clean user-provided login inputs
from typing import Dict, Any                  # Provides type hints (for better clarity)

class LoginHandler:
    """Handle user login functionality by verifying phone number and checking if PIN matched"""
    
    def __init__(self, db_manager: DatabaseManager = None):
        self.db_manager = db_manager or DatabaseManager()  # Initialize database manager

        self.validator = InputValidator()   # Initialize the input validator

    
    def authenticate_user(self, phone_number: str, pin: str = None) -> Dict[str, Any]:
        """
        Authenticates user in a two-step login process.

        Step 1: Validate and check if phone number exists
        Step 2: If PIN is provided, verify it against the stored value
        """
        try:
            # Clean and format inputs
            country_code = "+63" 
            phone_number = self.validator.clean_phone_number(phone_number)
            
            # Validate phone number format
            if not self.validator.validate_phone_number(phone_number):
                return {"success": False, "message": "Invalid phone number format."}
            
            # Combine country code and phone number (for matching in database)
            full_phone_number = country_code + phone_number
            
            # Check if user with that phone number exists
            user_data = self.db_manager.execute_query(
                '''SELECT id, first_name, last_name, country_code, phone_number, pin 
                   FROM users WHERE phone_number = ?''',
                (full_phone_number,)
            )
            
            # If no matching user was found, print an error message
            if not user_data:
                return {"success": False, "message": "User not found"}
            
            user = user_data[0]  # Get first (and only) result
            
            # Step 1: If no pin entered, confirm if phone number/user exists
            if pin is None:
                return {
                    "success": True, 
                    "message": "User found. Please enter your PIN.",
                    "step": 1
                }
            
            # Step 2: Verify PIN
            if not self.validator.validate_pin(pin):
                return {"success": False, "message": "PIN must be exactly 4 digits."}
            
            # Unpack user details
            user_id, first_name, last_name, db_country_code, db_phone, db_pin = user
            
            if pin != db_pin:  # Compare provided PIN with stored PIN
                return {"success": False, "message": "Incorrect PIN. Please try again."}
            
            # Successful login, return user info
            return {
                "success": True,
                "message": "Login successful!",
                "user_data": {
                    "id": user_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "country_code": db_country_code,
                    "phone_number": db_phone
                }
            }
                
        except Exception as e:   # Catch and return any unexpected error during login process

            return {"success": False, "message": f"Login error: {str(e)}"}