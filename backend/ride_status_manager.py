import uuid
import datetime
from backend.database_manager import DatabaseManager

def _now_iso() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")

# Create a new pending booking
def create_pending_booking(
    db: DatabaseManager,
    user_phone: str,
    vehicle_id: str,
    vehicle_type: str,
    driver_name: str,
    license_plate: str,
    distance: float,
    fare: float,
    pickup: str,
    dropoff: str,
) -> str:
    booking_id = str(uuid.uuid4())
    db.add_pending_booking(
        (
            booking_id,
            user_phone,
            vehicle_id,
            vehicle_type,
            driver_name,
            license_plate,
            distance,
            fare,
            pickup,
            dropoff,
            _now_iso(),
        )
    )
    return booking_id

# Move a booking from pending to cancelled
def cancel_booking(db: DatabaseManager, booking_id: str):
    rows = db.execute_query(
        "SELECT * FROM pending_bookings WHERE booking_id = ?", (booking_id,)
    )
    if not rows:
        print(f"❌ Booking {booking_id} not found.")
        return
    booking = rows[0]
    db.execute_update(
        "INSERT INTO cancelled_bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        booking,
    )
    db.delete_booking("pending_bookings", booking_id)
    print(f"✅ Booking {booking_id} has been cancelled.")

# Move a booking from pending to completed
def complete_booking(db: DatabaseManager, booking_id: str):
    rows = db.execute_query(
        "SELECT * FROM pending_bookings WHERE booking_id = ?", (booking_id,)
    )
    if not rows:
        print(f"❌ Booking {booking_id} not found.")
        return
    booking = rows[0]
    db.execute_update(
        "INSERT INTO completed_bookings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        booking,
    )
    db.delete_booking("pending_bookings", booking_id)
    print(f"✅ Booking {booking_id} marked as completed.")

# Get completed bookings for a specific user
def get_completed_bookings(db: DatabaseManager, user_phone: str):
    rows = db.get_bookings("completed_bookings", user_phone)
    bookings = []
    for row in rows:
        try:
            price_text = f"₱{float(row[7]):.2f}"
        except (ValueError, TypeError):
            price_text = str(row[7])
        bookings.append({
            "pickup": row[8],
            "dropoff": row[9],
            "vehicle": row[3],
            "price": price_text
        })
    return bookings

# Get canceled bookings for a specific user
def get_canceled_bookings(db: DatabaseManager, user_phone: str):
    rows = db.get_bookings("cancelled_bookings", user_phone)
    bookings = []
    for row in rows:
        try:
            price_text = f"₱{float(row[7]):.2f}"
        except (ValueError, TypeError):
            price_text = str(row[7])
        bookings.append({
            "pickup": row[8],
            "dropoff": row[9],
            "vehicle": row[3],
            "price": price_text
        })
    return bookings
