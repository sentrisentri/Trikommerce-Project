import csv

def generate_report(inventory_records):
    report_header = [("Day", "Sold Units", "Restocked Units", "Available Units")]
    report = report_header + inventory_records
    
    with open('inventory_report_Tshirts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(report)