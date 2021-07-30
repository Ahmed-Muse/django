from django.contrib import admin

# Register your models here.
from .models import *

from .forms import *

class CustomerCreateAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'project_name','project_status',
                'customer_contacts','contact_person','customer_address']#cant change this name...I think
                    #the reason is that they are functions and here we are only setting them up
    form = CustomerCreateForm
    list_filter = ['customer_name','customer_address']# this is the filter....you can not give this another name
    search_fields = ['customer_name', 'project_name']#this is the search fields....you can not give this another name

#register the customers model here
admin.site.register(AllifmaalCustomersTable,CustomerCreateAdmin)

class AddStockAdmin(admin.ModelAdmin):
    list_display = ['part_number', 'description', 'quantity_in_store','price','comments']#cant change this name...I think
                    #the reason is that they are functions and here we are only setting them up
    form = AddStockForm
    list_filter = ['part_number', 'description', 'quantity_in_store','price','comments']# this is the filter....you can not give this another name
    search_fields = ['part_number', 'description']#this is the search fields....you can not give this another name

#register the customers model here
admin.site.register(AllifmaalStockTable1,AddStockAdmin)

#to login is allifmaal and upto id
admin.site.register(Sale)


#below is for the invoice part..
#below code customizes the the look of the admin page
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'invoice_number', 'invoice_date']
    form = InvoiceForm
    list_filter = ['customer_name']
    search_fields = ['customer_name', 'invoice_number']
#admin.site.register(InvoiceTable)
admin.site.register(InvoiceTable, InvoiceAdmin)
