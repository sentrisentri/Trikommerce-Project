import random
import csv
import os
from IMS_simulation import run_simulation
from report_generation import generate_report
from unit_test import report_check

def main():
    total_days = 50
    inventory_records = []

    while True:
        print("1. Generate Report")
        print("2. Report Check")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            run_simulation(total_days, inventory_records)
            generate_report(inventory_records)
            print("Report generated successfully.")
        elif choice == '2':
            report_check()
            print("Done")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
