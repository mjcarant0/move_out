"""
This module handles validation and formatting of user inputs before interacting 
with the database. It ensures input data such as names, phone numbers, and PINs 
meet expected formats and values.
"""

import re  # Used for pattern matching and string cleaning operations

class InputValidator:
   
    # Implemented static methods to validate and format user input fields
    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        """Validate phone number format"""
        cleaned = InputValidator.clean_phone_number(phone_number)
        return cleaned.isdigit() and len(cleaned) == 10  # Must contain digits only and between 7–15 characters

    
    @staticmethod
    def validate_pin(pin: str) -> bool:
        """Validate pin format"""
        return pin.isdigit() and len(pin) == 4  #Must be numeric and exactly 4 characters

    @staticmethod
    def validate_pin_confirmation(pin: str, confirm_pin: str) -> bool:  
        """Validate that PIN and confirmation PIN match."""
        return pin == confirm_pin   # Ensure the confirmation PIN matches the original PIN
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate name"""
        return bool(name.strip()) and re.match(r'^[a-zA-Z\s]+$', name.strip())   # No numbers or symbols allowed
    
    @staticmethod
    def clean_phone_number(phone_number: str) -> str:
        """Clean phone number by removing spaces, dashes, and parentheses."""
        return re.sub(r'[\s\-\(\)]', '', phone_number)
    
    @staticmethod
    def format_name(name: str) -> str:
        """Format name to title case."""
        return name.strip().title()
    
    @staticmethod
    def format_phone_number(phone_number: str) -> str:
        """
        Convert a 10-digit PH number (e.g., 9082714653) into +63 format (e.g., +639082714653).
        """
        cleaned = InputValidator.clean_phone_number(phone_number)

        if len(cleaned) == 10 and cleaned.isdigit():
            return "+63" + cleaned
        elif cleaned.startswith("+63") and len(cleaned) == 13:
            return cleaned
        else:
            return cleaned  # Return as-is if already +63 or invalid
