import csv
from utils import delete_existing_report
from report_generation import generate_report
from IMS_simulation import run_simulation

def check_report_correctness():
    file = "inventory_report_Tshirts.csv"
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list(reader)
    
    total_restocked = 0
    total_sold = 0
    restock_days = set()
    
    for row in data:
        day_str, sold_units, restocked_units, remaining_units = row
        day = int(day_str)
        
        if day < 0 or day > 49:
            print(f"Error: Day {day} out of range in file {file}")
            return
        
        if int(restocked_units) > 2000 or int(remaining_units) > 2000:
            print(f"Error: Units exceed 2000 in file {file} on day {day}")
            return
        
        total_restocked += int(restocked_units)
        total_sold += int(sold_units)
        
        if int(restocked_units) > 0:
            restock_days.add(day)
    
    for expected_restock_day in range(7, 51, 7):
        if expected_restock_day not in restock_days:
            print(f"Error: Missing restock on day {expected_restock_day} in file {file}")
            return
    
    last_remaining_units = int(data[-1][3])
    if total_restocked - total_sold - last_remaining_units != 0:
        print(f"Error: Totals do not match in file {file}")
        return
    
    print(f"ALL CHECKS PASSED :) for file {file}")

def report_check():
    total_days = 50
    inventory_records = []
    delete_existing_report()
    inventory_records.clear()
    run_simulation(total_days, inventory_records)
    generate_report(inventory_records)
    check_report_correctness()