# Invoice Manager API

## Project Overview

The **Invoice Manager API** is a Django-based application designed for efficient invoice management. It allows users to search invoices by seller and date, calculate total receivables, and upload invoice data in bulk. The application supports invoice files in both PDF and image formats. With its robust API endpoints and admin interface, the project is built to handle a large volume of invoices with ease and accuracy.

---

## Features

- **Search Invoices**:
  - Search invoices by seller name and date.
  - Calculate the total receivable amount for a specified seller.
- **Invoice Storage**:
  - Store invoices as image files (PNG, JPG) or PDFs.
- **Bulk Upload**:
  - Upload multiple invoices using a CSV file via a custom Django management command.
- **Admin Interface**:
  - View, add, edit, and delete invoices through Django's admin interface.
- **Performance Optimization**:
  - Built to handle large datasets efficiently.
- **Unit Testing**:
  - Includes test cases to validate API functionality.

---

## Prerequisites

Ensure that you have the following installed:

- **Python 3.8+**
- **Django 4.2+**
- **Pillow** (for image handling)
- **SQLite** (default database, can be replaced with PostgreSQL or MySQL)

---

## Check your installed versions with:
```bash
python --version
django-admin --version

---

## Apply Migrations:
```bash
python manage.py migrate

## Create a Superuser:
```bash
python manage.py createsuperuser
Follow the prompts to create an admin account.

## Run the Server:
```bash
python manage.py runserver
The API will be available at http://127.0.0.1:8000.

## Usage

### 1. Search Invoices
**Endpoint:** `/api/invoices/search/`  
**Request Parameters:**
- `seller` (string): Name of the seller.
- `date` (string): Invoice date in `YYYY-MM-DD` format.

**Example Request:**
```http
GET /api/invoices/search/?seller=ABC&date=2024-11-01

Response:

json
{
  "seller": "ABC",
  "date": "2024-11-01",
  "total_receivable": 500,
  "invoices": [
    {
      "id": 1,
      "amount": 500.0,
      "file": "/media/invoices/abc_invoice_1.pdf"
    }
  ]
}

### 2. Bulk Upload Invoices
Upload multiple invoices via a CSV file using the `import_invoices` management command.

**CSV Format:**
```csv
seller_name,invoice_date,amount,file
ABC,2024-11-01,500.0,invoices/abc_invoice_1.pdf
XYZ,2024-11-02,300.5,invoices/xyz_invoice_2.png
DEF,2024-11-03,750.0,invoices/def_invoice_3.pdf
Command:

bash
python manage.py import_invoices <path_to_csv_file>
Example:

bash
python manage.py import_invoices demo_invoices.csv

bash
python manage.py import_invoices <path_to_csv_file>

3. Admin Interface
Access the admin interface at: http://127.0.0.1:8000/admin/ Log in using the superuser credentials to add, edit, delete, or view invoices.

### 4. Unit Tests
Run the included tests to validate the API:
```bash
python manage.py test
## File Structure
bash
InvoiceManager/
├── invoices/
│   ├── admin.py       # Admin interface for managing invoices
│   ├── models.py      # Database models
│   ├── views.py       # API views
│   ├── tests.py       # Unit tests
│   ├── management/
│   │   ├── commands/
│   │       ├── import_invoices.py  # Bulk upload command
├── InvoiceManager/
│   ├── settings.py    # Django settings
│   ├── urls.py        # URL routing
│   ├── wsgi.py        # WSGI application
├── media/             # Uploaded invoice files
├── manage.py          