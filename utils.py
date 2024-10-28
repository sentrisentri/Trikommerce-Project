import os

def delete_existing_report():
    file = "inventory_report_Tshirts.csv"
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} deleted.")
    else:
        print(f"{file} does not exist.")