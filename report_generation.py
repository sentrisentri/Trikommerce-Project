import csv
from restock import restock_inventory
from sales import daily_sales

def generate_report(inventory_records):
    # Initialize variables
    available_items = 2000
    inventory_records = []

    # Iterate through days
    for current_day in range(50):
        if current_day % 7 == 0:  # Restocking day
            available_items = restock_inventory(available_items, inventory_records, current_day)
        else:  # Selling day
            available_items = daily_sales(available_items, inventory_records, current_day)

    # Write to CSV file
    with open('inventory_report_Tshirts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Day', 'Sold Units', 'Restocked Units', 'Available Units'])
        # Write records
        writer.writerows(inventory_records)

    print(inventory_records)
