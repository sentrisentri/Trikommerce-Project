import random  # For generating random values (if used in simulation or elsewhere)
import csv  # For reading and writing CSV files
import os  # For file system operations
from IMS_simulation import run_simulation  # Function to simulate inventory management
from report_generation import generate_report  # Function to generate an inventory report
from unit_test import report_check  # Function to validate the correctness of the generated report

def main():
    """
    Main function that provides a user interface for managing inventory simulation and report generation.
    """
    total_days = 50  # Total number of days for the simulation
    inventory_records = []  # List to hold inventory records during the simulation

    # Run a loop to provide a menu-driven interface
    while True:
        # Display menu options
        print("1. Generate Report")
        print("2. Report Check")
        print("3. Exit")
        
        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Option to generate a new report
            run_simulation(total_days, inventory_records)  # Run the inventory simulation
            generate_report(inventory_records)  # Generate a report based on the simulation data
            print("Report generated successfully.")  # Confirm report generation to the user
        
        elif choice == '2':
            # Option to check the correctness of the report
            report_check()  # Validate the generated report
            print("Done")  # Notify the user that the report check is complete
        
        elif choice == '3':
            # Option to exit the program
            break  # Exit the while loop, ending the program
        
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")  # Prompt the user to provide a valid input

# Ensure the main function is executed only when the script is run directly
if __name__ == "__main__":
    main()

