from data import bookings, parking_spaces
from parking import show_available_spaces
from users import read_positive_number


def book_space(driver):
    show_available_spaces()
    available_spaces = []
    for space in parking_spaces:
        if space["available"]:
            available_spaces.append(space)

    if not available_spaces:
        return

    try:
        selected_id = int(input("Enter the ID of the space to book: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    selected_space = None
    for space in available_spaces:
        if space["id"] == selected_id:
            selected_space = space
            break

    if selected_space is None:
        print("That ID is not an available parking space.")
        return
    if selected_space["owner"].lower() == driver.lower():
        print("You cannot book your own parking space.")
        return

    hours = read_positive_number("How many hours do you need the space? ")
    total_price = hours * selected_space["price_per_hour"]
    booking_id = len(bookings) + 1

    bookings.append(
        {
            "id": booking_id,
            "driver": driver,
            "owner": selected_space["owner"],
            "space_id": selected_space["id"],
            "location": selected_space["location"],
            "hours": hours,
            "total_price": total_price,
            "active": True,
        }
    )
    selected_space["available"] = False
    print(f"Booking confirmed. Booking ID: {booking_id}")
    print(f"Total price: Rs. {total_price:.2f}")


def show_my_bookings(driver):
    found_booking = False
    print(f"\nBookings for {driver}")

    for booking in bookings:
        if booking["driver"].lower() == driver.lower():
            found_booking = True
            if booking["active"]:
                status = "Active"
            else:
                status = "Cancelled"
            print(
                f"Booking ID: {booking['id']} | Location: {booking['location']} | "
                f"Owner: {booking['owner']} | Hours: {booking['hours']:g} | "
                f"Total: Rs. {booking['total_price']:.2f} | Status: {status}"
            )

    if not found_booking:
        print("You do not have any bookings yet.")


def cancel_booking(driver):
    active_bookings = []
    for booking in bookings:
        if booking["driver"].lower() == driver.lower() and booking["active"]:
            active_bookings.append(booking)

    if not active_bookings:
        print("You have no active bookings to cancel.")
        return

    show_my_bookings(driver)
    try:
        selected_id = int(input("Enter the booking ID to cancel: "))
    except ValueError:
        print("Please enter a valid booking ID.")
        return

    selected_booking = None
    for booking in active_bookings:
        if booking["id"] == selected_id:
            selected_booking = booking
            break

    if selected_booking is None:
        print("That is not one of your active bookings.")
        return

    selected_booking["active"] = False
    for space in parking_spaces:
        if space["id"] == selected_booking["space_id"]:
            space["available"] = True
            break

    print("Booking cancelled. The parking space is available again.")
