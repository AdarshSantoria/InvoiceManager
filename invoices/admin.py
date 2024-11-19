from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('seller_name', 'invoice_date', 'amount', 'file')
    list_filter = ('seller_name', 'invoice_date')
    search_fields = ('seller_name',)
    actions = ['delete_selected_invoices']

    def delete_selected_invoices(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} invoice(s) deleted successfully.")

    delete_selected_invoices.short_description = "Delete selected invoices"
