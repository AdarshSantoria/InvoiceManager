import csv

# Define sample invoice data
invoices = [
    {"seller_name": "ABC", "invoice_date": "2024-11-01", "amount": "500.0", "file": "invoices/abc_invoice_1.pdf"},
    {"seller_name": "XYZ", "invoice_date": "2024-11-02", "amount": "300.5", "file": "invoices/xyz_invoice_2.png"},
    {"seller_name": "DEF", "invoice_date": "2024-11-03", "amount": "750.0", "file": "invoices/def_invoice_3.pdf"},
]

# Path for the demo CSV file
demo_csv_path = "demo_invoices.csv"

# Create the CSV file
with open(demo_csv_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["seller_name", "invoice_date", "amount", "file"])
    writer.writeheader()  # Write the header row
    writer.writerows(invoices)  # Write the data rows

print(f"Demo CSV file created at: {demo_csv_path}")
