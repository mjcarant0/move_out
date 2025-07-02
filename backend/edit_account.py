"""
This module handles editing user account information and changing user PINs.
It performs validation and database updates using InputValidator and DatabaseManager.
"""

from database_manager import DatabaseManager   # Handles queries and updates to the user database
from validators import InputValidator          # Validates and formats input fields before saving
from typing import Dict, Any, Optional         # Provides type annotations for clarity

class EditAccountHandler:
    """
    Handle user account editing functionality.
    """
    
    def __init__(self, db_manager: DatabaseManager = None):
        self.db_manager = db_manager or DatabaseManager()
        self.validator = InputValidator()
    
    def update_user(self, old_phone_number: str, first_name: str = None, 
                   last_name: str = None, new_country_code: str = None,
                   new_phone_number: str = None) -> Dict[str, Any]:
        """
        Handle user account editing. Return status and message.
        """
        try:
            # Check if user exists based on old phone number
            user_data = self.db_manager.execute_query(
                "SELECT ID from users where phone_number = ?", 
                (old_phone_number,)
            )
            
            if not user_data:
                return {"success": False, "message": "User not found."}  # 
            
            user_id = user_data[0][0]
            updates = []
            values = []
            
            # If new first name is provided, validate and prepare update
            if first_name is not None:
                if not self.validator.validate_name(first_name):
                    return {"success": False, "message": "Invalid first name. Only letters and spaces allowed."}
                updates.append("first_name = ?")
                values.append(self.validator.format_name(first_name))
            
            # If new last name is provided, validate and perpare update
            if last_name is not None:
                if not self.validator.validate_name(last_name):
                    return {"success": False, "message": "Invalid last name. Only letters and spaces allowed."}
                updates.append("last_name = ?")
                values.append(self.validator.format_name(last_name))
            
            # If new phone number and country code are provided, validate both
            if new_country_code is not None and new_phone_number is not None:
                new_country_code = self.validator.format_country_code(new_country_code)  # Format the new country code (adds '+' if missing)

                new_phone_number = self.validator.clean_phone_number(new_phone_number)   # Remove extra symbols from the phone number

                # Check if the formatted country code is valid (must be in ASEAN list)
                if not self.validator.validate_country_code(new_country_code):
                    return {"success": False, "message": "Invalid country code."}
                
                # Check if the cleaned phone number has the correct format and length
                if not self.validator.validate_phone_number(new_phone_number):
                    return {"success": False, "message": "Invalid new phone number format."}
                
                full_new_phone = new_country_code + new_phone_number  # Combine both to store in database

                
                # Check if new phone number is already in use by another user 
                existing_user = self.db_manager.execute_query(
                    "SELECT id FROM users WHERE phone_number = ? AND id != ?",
                    (full_new_phone, user_id)
                )
                
                if existing_user:  # If another user has this number, don't allow update
                    return {"success": False, "message": "New phone number already in use by another account."}
                    
                # Prepare the update queries and values
                updates.append("country_code = ?")
                values.append(new_country_code)
                updates.append("phone_number = ?")
                values.append(full_new_phone)

            # If no fields provided, don't update anything
            if not updates:
                return {"success": False, "message": "No updates provided."}
            
            # Finalize query and execute the update
            values.append(user_id)  # Append user_id to match WHERE clause in the final query
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
            
            rows_affected = self.db_manager.execute_update(query, tuple(values))
            
            if rows_affected == 0:
                return {"success": False, "message": "No changes made."}
            
            return {"success": True, "message": "Account updated successfully!"}
                
        except Exception as e:
            return {"success": False, "message": f"Error updating account: {str(e)}"}
    
    def change_pin(self, phone_number: str, old_pin: str, new_pin: str) -> Dict[str, Any]:
        """
        Update user's PIN after verifying the current one.
        """
        try:
            # Validate both old and new PINs
            if not self.validator.validate_pin(old_pin): 
                return {"success": False, "message": "Invalid current PIN format."}
            
            if not self.validator.validate_pin(new_pin):
                return {"success": False, "message": "New PIN must be exactly 4 digits."}
            
            # Retrieve user and their stored PIN
            user_data = self.db_manager.execute_query(
                "SELECT id, pin FROM users WHERE phone_number = ?",
                (phone_number,)
            )
            
            if not user_data:
                return {"success": False, "message": "User not found."}
            
            user_id, current_pin = user_data[0]
            
            # Check if old PIN matches the stored one
            if old_pin != current_pin:
                return {"success": False, "message": "Current PIN is incorrect."}
            
            # Update PIN
            rows_affected = self.db_manager.execute_update(
                "UPDATE users SET pin = ? WHERE id = ?",
                (new_pin, user_id)
            )
            
            if rows_affected > 0:
                return {"success": True, "message": "PIN updated successfully!"}
            else:
                return {"success": False, "message": "Failed to update PIN."}
                
        except Exception as e:
            return {"success": False, "message": f"Error changing PIN: {str(e)}"}
