from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Invoice
from datetime import date

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        mock_pdf = SimpleUploadedFile("invoice1.pdf", b"Dummy PDF content", content_type="application/pdf")
        mock_png = SimpleUploadedFile("invoice2.png", b"Dummy PNG content", content_type="image/png")
        Invoice.objects.create(seller_name="ABC", invoice_date=date(2024, 11, 1), amount=500, file=mock_pdf)
        Invoice.objects.create(seller_name="XYZ", invoice_date=date(2024, 1, 1), amount=300, file=mock_png)

    def test_search_invoices(self):
        response = self.client.get('/api/invoices/search/', {'seller': 'ABC', 'date': '2024-11-01'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.json()['total_receivable']), 500.0)
