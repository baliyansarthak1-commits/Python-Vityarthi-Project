# Toll Booth Management System - main menu
# Run with:  python main.py
from booth import show_counts, update_count
from pricing import rates, get_toll
from records import receipts, add_receipt, get_total_cash
from rules import is_exempt
from reports import cash_alert

while True:
    ch = input("\n1.Rates 2.Ticket 3.Counts 4.Receipts 5.Alerts 6.Exit\nChoice: ").strip()

    if ch == "1":
        for v in rates:
            print(v, "- Single: Rs.", get_toll(v, "Single"),
                  "| Return: Rs.", get_toll(v, "Return"))

    elif ch == "2":
        plate = input("Plate No: ").strip().upper()
        if plate == "":
            print("Plate number cannot be empty!")
        elif is_exempt(plate):
            add_receipt(plate, "Exempt", 0)
            print("Emergency/VIP vehicle! Toll: Rs. 0")
        else:
            # .title() makes "car", "CAR" and "car " all become "Car"
            v = input("Type (Car/Bus/Truck): ").strip().title()
            if v in rates:
                trip = input("Trip (Single/Return): ").strip().title()
                while trip != "Single" and trip != "Return":
                    print("Invalid trip! Type Single or Return.")
                    trip = input("Trip (Single/Return): ").strip().title()
                toll = get_toll(v, trip)
                update_count(v)
                add_receipt(plate, v, toll)
                print("Toll to pay: Rs.", toll)
            else:
                print("Invalid vehicle type!")

    elif ch == "3":
        show_counts()

    elif ch == "4":
        if not receipts:
            print("No receipts issued yet.")
        for r in receipts:
            print(r["plate"], "-", r["type"], "- Rs.", r["amt"])
        print("Total Cash: Rs.", get_total_cash())

    elif ch == "5":
        total = get_total_cash()
        print("Cash in counter: Rs.", total)
        print(cash_alert(total))

    elif ch == "6":
        print("Shift ended. Bye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
