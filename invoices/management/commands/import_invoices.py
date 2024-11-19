import csv
from django.core.management.base import BaseCommand
from invoices.models import Invoice
from datetime import datetime

class Command(BaseCommand):
    help = "Import invoices from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Validate required fields
                    if not row.get('seller_name') or not row.get('invoice_date') or not row.get('amount') or not row.get('file'):
                        self.stderr.write(self.style.ERROR(f"Skipping invalid row: {row}"))
                        continue

                    # Create invoice
                    Invoice.objects.create(
                        seller_name=row['seller_name'],
                        invoice_date=datetime.strptime(row['invoice_date'], '%Y-%m-%d').date(),
                        amount=float(row['amount']),
                        file=row['file']
                    )
            self.stdout.write(self.style.SUCCESS("Invoices imported successfully!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing invoices: {e}"))
