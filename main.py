from bookings import book_space, cancel_booking, show_my_bookings
from parking import offer_parking_space, show_available_spaces
from users import get_user_name


def show_menu():
    print("\nPERSON-TO-PERSON PARKING SYSTEM")
    print("1. View available parking spaces")
    print("2. Offer my parking space")
    print("3. Book a parking space")
    print("4. View my bookings")
    print("5. Cancel a booking")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            show_available_spaces()
        elif choice == "2":
            owner = get_user_name("Enter your name: ")
            offer_parking_space(owner)
        elif choice == "3":
            driver = get_user_name("Enter your name: ")
            book_space(driver)
        elif choice == "4":
            driver = get_user_name("Enter your name: ")
            show_my_bookings(driver)
        elif choice == "5":
            driver = get_user_name("Enter your name: ")
            cancel_booking(driver)
        elif choice == "0":
            print("Thank you for using the parking system.")
            break
        else:
            print("Invalid choice. Please choose a menu number.")


if __name__ == "__main__":
    main()
