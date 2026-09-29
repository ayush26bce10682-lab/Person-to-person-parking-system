"""Functions for viewing and listing parking spaces."""

from data import parking_spaces
from users import read_positive_number


def show_available_spaces():
    """Print every parking space that can currently be booked."""
    found_space = False
    print("\nAvailable parking spaces")
    print("-" * 65)

    for space in parking_spaces:
        if space["available"]:
            found_space = True
            print(
                f"ID: {space['id']} | Owner: {space['owner']} | "
                f"Location: {space['location']} | Vehicle: {space['vehicle']} | "
                f"Rs. {space['price_per_hour']:.2f} per hour"
            )

    if not found_space:
        print("There are no available spaces right now.")


def offer_parking_space(owner):
    """Collect details from an owner and add a new available space."""
    print("\nOffer your parking space")
    location = input("Enter the location: ").strip()
    while not location:
        print("Location cannot be empty.")
        location = input("Enter the location: ").strip()

    vehicle = input("Vehicle type (Car/Bike/Other): ").strip()
    while not vehicle:
        print("Vehicle type cannot be empty.")
        vehicle = input("Vehicle type (Car/Bike/Other): ").strip()

    price = read_positive_number("Price per hour in rupees: ")
    new_id = 1
    for space in parking_spaces:
        if space["id"] >= new_id:
            new_id = space["id"] + 1

    parking_spaces.append(
        {
            "id": new_id,
            "owner": owner,
            "location": location,
            "vehicle": vehicle,
            "price_per_hour": price,
            "available": True,
        }
    )
    print(f"Your parking space is listed with ID {new_id}.")
