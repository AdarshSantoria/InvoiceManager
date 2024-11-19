from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    if not value.name.lower().endswith(('.png', '.pdf')):
        raise ValidationError('File must be a PNG image or PDF.')

class Invoice(models.Model):
    seller_name = models.CharField(max_length=255)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='invoices/', blank=False, null=False, validators=[validate_file_extension])

    def __str__(self):
        return f"{self.seller_name} - {self.invoice_date} - ${self.amount}"
