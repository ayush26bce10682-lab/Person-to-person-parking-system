# Person to Person Parking System

A beginner Python command-line project for sharing privately owned parking spaces. Owmers can list spaces; drivers can browse, book by the hour and cancel a booking.

## Course alignment 

Designed for Introduction to Problem Solving and Program (CSE1021). The implementation functions, conditions, loops, input validation, lists, dictionaries and simple algorithms.

##Features

- View available spaces with location, vehicle type, owner and hourly price.
- Offer a parking space using a unique numeric ID.
- Book another person's available space for a positive number of hours.
- Calculate and display the total price.
- View bookings by the entered driver name and cancel an active booking.
- Return a cancelled space to the available list.

## Files

person_to_person_parking/
|--- main.py                 #Menu and application flow
|--- users.py                #Name and positive-number input helpers

|--- parkings.py             # View and offer parking spaces
|--- bookings.py             # Book, view, and cancel bookings
|--- data.py                  #Samples spaces and in memory bookings list
|--- README.md
|--- statement.md            


the five Python files are the complete source code.The Markdown files and report are submisson documentation

## Requirements and run steps 

- Python 3.8 or newer; no third-party packages are required .
-Open a terminal in this folder and run:
'''bash
python main.py
'''


On some systems, use 'python3 main.py' instead

## Typical workflow 

1. Choose **View available parking spaces** to see the sample listings 
2. Choose **Book a parking space**, enter a driver name, select a space ID, and enter the number of hours.
3. Choose **View my booking** to see booking id and calculated total
4. Choose **Cancel bookings** and enter the booking ID to release the space.
5. An owner can choose **Offer my parking space** to add a listing.

##  Manual validation chacklist

- Book Asha's space(ID 1) as another user for 2 hours ; the total should be rs 60.00. 
- View the driver's bookings and confirm that the booking is active.
- Cancel that booking and confirm that the space appears as available again.
- Try an invalid input menu option, a non numeric booking ID, blank text, and a zero or negative price/duration; the program should show an error and continue safely.
- Try to book a space using the same name shown as its owner; the program should reject the self booking.

## Design overview

```mermaid 
flowchar LR 
    U[Owner or driver] --> M[main.py menu]
    M --> P[parking.py]
    M --> B[bookings.py]
    P --> D[data.py lists]
    B --> D
    P --> V[users.py validation]
    B --> V
```
The app keeps two Python list in `data.py`: a list of parking-space dictionaries and a list of booking dictationaries. This keeps the data model visible for beginner study. All data is in memory and resetswhen the program exits; this  version has no database, account authentication, or payement processings.


## Non functional Requirements 

- **Usability:** numbered menu, direct prompts, and readable price totals.
- **Reliability** validates empty names and descriptions , numeric values, ID's, booking ownerships, and availability.
- **Maintainability:** seprates menu, input helpers ,parking actions,bookings action,and sample data into five modules.
- **Performance**  simplelist searches and approppriate for a small classroom demonstaration; the expected lookup time grows linearly with the numbers of records.
- **Privacy and security :** the program collects no passwords , payement details, or contact information. Names are self entered and are not authtenticated , so this demonstration must not be used to protect real blockings.  


