from django.http import JsonResponse
from django.db.models import Sum
from django.shortcuts import get_list_or_404
from .models import Invoice

def search_invoices(request):
    seller = request.GET.get('seller', None)
    date = request.GET.get('date', None)
    if not seller or not date:
        return JsonResponse({"error": "Missing 'seller' or 'date' parameter"}, status=400)

    try:
        invoices = Invoice.objects.filter(seller_name__icontains=seller, invoice_date=date)
        total_amount = invoices.aggregate(total=Sum('amount'))['total'] or 0
        return JsonResponse({
            "seller": seller,
            "date": date,
            "total_receivable": total_amount,
            "invoices": [
                {"id": invoice.id, "amount": float(invoice.amount), "file": invoice.file.url}
                for invoice in invoices
            ],
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
