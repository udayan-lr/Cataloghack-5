stations = [
    {"name": "FastCharge", "location": "Downtown", "connector_types": ["Type 1", "Type 2"], "available_slots": 5},
    {"name": "EcoCharge", "location": "Uptown", "connector_types": ["Type 2", "CCS"], "available_slots": 2},
    {"name": "QuickCharge", "location": "Midtown", "connector_types": ["CHAdeMO", "CCS"], "available_slots": 3},
    {"name": "GreenCharge", "location": "Suburbs", "connector_types": ["Type 1", "CHAdeMO"], "available_slots": 4},
]
def find_stations(location=None, connector_type=None):
    print("Available Charging Stations:")
    for station in stations:
        if (location is None or station["location"].lower() == location.lower()) and \
           (connector_type is None or connector_type in station["connector_types"]):
            print(f"Station: {station['name']}, Location: {station['location']}, Connector Types: {', '.join(station['connector_types'])}, Available Slots: {station['available_slots']}")
    print()
def book_slot(station_name):
    for station in stations:
        if station["name"].lower() == station_name.lower():
            if station["available_slots"] > 0:
                station["available_slots"] -= 1
                print(f"Slot booked at {station['name']}. Slots remaining: {station['available_slots']}\n")
                return
            else:
                print(f"No slots available at {station['name']}.\n")
                return
    print("Charging station not found.\n")
print("Welcome to the EV Charging Station Finder and Slot Booking System")
while True:
    print("1. Find Charging Stations")
    print("2. Book a Charging Slot")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        loc = input("Enter location to filter by (or press Enter to skip): ")
        conn_type = input("Enter connector type to filter by (or press Enter to skip): ")
        find_stations(loc if loc else None, conn_type if conn_type else None)
    elif choice == "2":
        station_name = input("Enter the name of the station to book a slot: ")
        book_slot(station_name)
    elif choice == "3":
        print("Thank you for using the EV Charging Station Finder and Slot Booking System!")
        break
    else:
        print("Invalid option, please try again.\n")
