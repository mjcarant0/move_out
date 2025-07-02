from database_manager import DatabaseManager

def cancel_booking(db: DatabaseManager, booking_id: str):
    """Cancel a ride by moving it from pending to cancelled bookings."""
    result = db.execute_query(
        "SELECT * FROM pending_bookings WHERE booking_id = ?", (booking_id,)
    )

    if not result:
        print(f"❌ Booking {booking_id} not found.")
        return

    booking = result[0]

    db.execute_update(
        "INSERT INTO cancelled_bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        booking
    )

    db.execute_update(
        "DELETE FROM pending_bookings WHERE booking_id = ?",
        (booking_id,)
    )

    print(f"✅ Booking {booking_id} has been cancelled.")


def complete_booking(db: DatabaseManager, booking_id: str):
    """Mark a ride as completed by moving it from pending to completed bookings."""
    result = db.execute_query(
        "SELECT * FROM pending_bookings WHERE booking_id = ?", (booking_id,)
    )

    if not result:
        print(f"❌ Booking {booking_id} not found.")
        return

    booking = result[0]

    db.execute_update(
        "INSERT INTO completed_bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        booking
    )

    db.execute_update(
        "DELETE FROM pending_bookings WHERE booking_id = ?",
        (booking_id,)
    )

    print(f"✅ Booking {booking_id} marked as completed.")