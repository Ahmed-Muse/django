from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import sys
from django.core.mail import send_mail#this is for sending email from contact form




#for exporting data in CSV format
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required#required for login to work
from django.core.files.storage import FileSystemStorage#for storing uploaded files
from .utils import get_plot#for ploting
import numpy as np
import matplotlib.pyplot as plt
import json
def index(request):
    title="Allifmaal System"
    query_table_content = AllifmaalCustomersTable.objects.all()#assign all the objects in the table to the variable

    context = {
	"title": title,
    "query_table_content":query_table_content
	}#context contains the number of variables to be passed/called to the html templates/pages
    #so basically we are telling the views to pass whatever is contained in the context to the index.html page.

    return render(request,'index.html',context)
#@login_required
def customers(request):
    title="Allifmaal Customers"
    query_table_content = AllifmaalCustomersTable.objects.all()#assign all the objects in the table to the variable

    context = {
	"title": title,
    "query_table_content": query_table_content
	}


    # start of the search form part.............................
    form = CustomerSearchForm(request.POST or None)#this is for the search
    if request.method == 'POST':
    	query_table_content = AllifmaalCustomersTable.objects.filter(customer_name__icontains=form['customer_name'].value(),
									project_name__icontains=form['project_name'].value())
    context = {#without context, you will not see the form in the page
	    "form": form,

	    "query_table_content": query_table_content,
                }

    #end of search form pat.................................

    return render(request,'customers.html',context)

def add_customers(request):
    title="Add Customers"
    form=CustomerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
    context = {
	"title": "Add Customer",
 "form": form,
 "title":title,

	}

    return render(request,'add_customers.html',context)


#add products
def add_stock(request):
    title="Add Stock"
    form=AddStockForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Stock added successfully')
    context = {
	"title": "Add Stock",
 "form": form

	}

    return render(request,'add_stock.html',context)

#@login_required
def stock(request):
    header="Allifmaal Stock Management System "
    query_table_content = AllifmaalStockTable1.objects.all()#assign all the objects in the table to the variable

    context = {
	"header": header,
    "query_table_content": query_table_content
	}

    # start of the search form part.............................
    form = StockSearchForm(request.POST or None)#this is for the search
    if request.method == 'POST':
    	query_table_content = AllifmaalStockTable1.objects.filter(part_number__icontains=form['part_number'].value(),
									description__icontains=form['description'].value())
     #End of search

     #start of section for exporting data in CSV format
    if form['csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            ''' writer = csv.writer(response)#this is showing error so comments out all
            writer.writerow(['PART_NUMBER', 'DESCRIPTION', 'QUANTITY_IN_STORE','PRICE','COMMENTS'])
            instance = query_table_content
            for stock in instance:
                writer.writerow([stock.part_number, stock.description,stock.quantity_in_store,stock.price,stock.comments])
            return response '''

        ### end of section for exporting data in CSV format


    context = {#without context, you will not see the form in the page
	    "form": form,

	    "query_table_content": query_table_content,
                }

    #end of search form pat.................................

    return render(request,'stock.html',context)


def add_staff(request):
    form=AddStaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Staff added successfully')
    context = {
	"title": "Add Staff",
    "form": form

	}

    return render(request,'add_staff.html',context)
#@login_required
def hrm(request):
    header="Allifmaal HRM Management System "
    query_table_content = AllifmaalHRMTable.objects.all()#assign all the objects in the table to the variable

    context = {
	"header": header,
    "query_table_content": query_table_content
	}

    # start of the search form part.............................
    form = StaffSearchForm(request.POST or None)#this is for the search
    if request.method == 'POST':
    	query_table_content = AllifmaalHRMTable.objects.filter(staff_number__icontains=form['staff_number'].value(),
									first_name__icontains=form['first_name'].value())
    context = {#without context, you will not see the form in the page
	    "form": form,

	    "query_table_content": query_table_content,
                }
    #end of search form pat.................................

    return render(request,'hrm.html',context)


#@login_required
def dashboard(request):
    header="Allifmaal Sales Management System"

    context = {
	"header": header,

	}

    return render(request,'dashboard.html',context)
#@login_required
def eshop(request):
    header="Allifmaal Online Shop Management System"

    context = {
	"header": header,

	}
    return render(request,'eshop.html',context)


# UPDATE SECTIONS
def update_customers(request, pk):
    query_table_content= AllifmaalCustomersTable.objects.get(id=pk)
    form = CustomerUpdateForm(instance=query_table_content)#insert the content of the table stored in the selected id in the update form
    #we could have used the add customer form but the validation will refuse us to update since fields may exist
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=query_table_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully')
            return redirect('/customers')
    context = {
		'form':form
    }
    return render(request, 'add_customers.html', context)

# add the url below in the urls file
''' path('update_items/<str:pk>/', views.update_items, name="update_items"), '''

def update_stock(request, pk):
    query_table_content= AllifmaalStockTable1.objects.get(id=pk)
    form = StockUpdateForm(instance=query_table_content)#insert the content of the table stored in the selected id in the update form
    #we could have used the add customer form but the validation will refuse us to update since fields may exist
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=query_table_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock updated successfully')
            return redirect('/stock')
    context = {
		'form':form
    }
    return render(request, 'add_stock.html', context)

# add the url below in the urls file
''' path('update_items/<str:pk>/', views.update_items, name="update_items"), '''

def update_staff(request, pk):
    query_table_content= AllifmaalHRMTable.objects.get(id=pk)
    form = StaffUpdateForm(instance=query_table_content)#insert the content of the table stored in the selected id in the update form
    #we could have used the add customer form but the validation will refuse us to update since fields may exist
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, instance=query_table_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff record updated successfully')
            return redirect('/hrm')
    context = {
		'form':form
    }
    return render(request, 'add_staff.html', context)

# add the url below in the urls file
''' path('update_items/<str:pk>/', views.update_items, name="update_items"), '''


#########  DELETE SECTION .................
def delete_customer(request,pk):
    query_table_content=AllifmaalCustomersTable.objects.get(id=pk)
    if request.method =="POST":
        query_table_content.delete()
        messages.success(request,'Record deleted successfully')
        return redirect('/customers')
    return render(request,'delete_customer.html')	#return render(request, 'delete_customer.html')

def delete_stock(request,pk):
    query_table_content=AllifmaalStockTable1.objects.get(id=pk)
    if request.method =="POST":
        query_table_content.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('/stock')
    return render(request,'delete_stock.html')


def delete_staff(request,pk):
    query_table_content=AllifmaalHRMTable.objects.get(id=pk)
    if request.method =="POST":
        query_table_content.delete()
        messages.success(request,'Staff record deleted successfully')
        return redirect('/hrm')
    return render(request,'delete_staff.html')

##########3... END DELETE SECTION


def stock_details(request, pk):
    query_table_content = AllifmaalStockTable1.objects.get(id=pk)
    context = {

		"query_table_content": query_table_content,
	}
    return render(request, "stock_details.html", context)


#ISSUE AND RECEIVE SECTIONS

def issue_items(request, pk):
    query_table_content = AllifmaalStockTable1.objects.get(id=pk)
    form = IssueItemForm(request.POST or None, instance=query_table_content)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.receive_quantity=0
        instance.quantity_in_store -= instance.issue_quantity
        #instance.quantity=instance.quantity - instance.issue_quantity

        #instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity_in_store) + " " + str(instance.part_number) + "s now left in Store")
        instance.issue_by=str(request.user)
        instance.save()

        return redirect('/stock_details/'+str(instance.id))
    context = {
		"title": 'Issue ' + str(query_table_content.part_number),
		"query_table_content": query_table_content,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
    return render(request, "add_stock.html", context)

#receive sections
def receive_items(request, pk):
    query_table_content = AllifmaalStockTable1.objects.get(id=pk)
    form = ReceiveItemForm(request.POST or None, instance=query_table_content)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_quantity=0
        instance.quantity_in_store+=instance.receive_quantity
        instance.receive_by=str(request.user)
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity_in_store) + " " + str(instance.part_number)+"s now in Store")
        return redirect('/stock_details/'+str(instance.id))
    context = {
			"title": 'Receive ' + str(query_table_content.part_number),
			"query_table_content": query_table_content,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
    return render(request, "add_stock.html", context)

#reorder level view
def reorder_level(request,pk):
    query_table_content =AllifmaalStockTable1.objects.get(id=pk)
    form=StockReorderLevelForm(request.POST or None,instance=query_table_content)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for" + str(instance.description) + " is updated to   " + str(instance.reorder_level))
        return redirect('/stock')
    context={
        "instance":query_table_content,
        "form":form,
    }
    return render(request,"add_stock.html",context)

#view for history table
#@login_required
def stock_history(request):
    header = 'LIST OF ITEMS'
    query_table_content = AllifmaalStockHistoryTable.objects.all()
    form=StockHistorySearchForm(request.POST or None)

    if request.method == 'POST':
        query_table_content = AllifmaalStockHistoryTable.objects.filter(
	    description__icontains=form['description'].value(),

	)
    """ if request.method == 'POST':
        query_table_content = AllifmaalStockHistoryTable.objects.filter(
	    description__icontains=form['description'].value(),
	    last_updated__range=[
							form['start_date'].value(),
							form['end_date'].value()
						]
	) """

    context = {
		"header": header,
		"query_table_content": query_table_content,
        "form":form,
	}
    return render(request, "stock_history.html",context)


#delete records of history table
def delete_history_record(request,pk):
    query_table_content=AllifmaalStockHistoryTable.objects.get(id=pk)
    if request.method =="POST":

        query_table_content.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('/stock')
    return render(request,'delete_history_record.html')



#view for creating category
def add_category(request):
    form_category = CategoryCreateForm(request.POST or None)
    if form_category.is_valid():
        form_category.save()
        messages.success(request, 'Successfully has been created')
        #return redirect('/stock')
    context = {
		"form": form_category,
		"title": "Add Category",
	}
    return render(request, "add_stock.html", context)


#calculator page

def calc(request):
    title="calculator"

    context = {

 "title":title,

	}

    return render(request,'calc.html',context)

def vehicles(request):
    header="Allifmaal Online Shop Management System"
    query_table_content = AllifmaalVehiclesTable1.objects.all()
    if request.method == 'POST':
        form=AddVehicleDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle added successfully')
            return redirect('vehicles')
    else:
        form=AddVehicleDetailsForm()

    context = {
	"header": header,
    "form":form,
    "query_table_content":query_table_content,

	}
    return render(request,'vehicles.html',context)

def delete_vehicle(request,pk):
    query_table_content=AllifmaalVehiclesTable1.objects.get(id=pk)
    if request.method =="POST":
        query_table_content.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('/vehicles')
    return render(request,'delete_vehicle.html')


def update_vehicle_details(request, pk):
    query_table_content= AllifmaalVehiclesTable1.objects.get(id=pk)
    form = VehicleDetailsUpdateForm(instance=query_table_content)#insert the content of the table stored in the selected id in the update form
    #we could have used the add customer form but the validation will refuse us to update since fields may exist
    if request.method == 'POST':
        form = VehicleDetailsUpdateForm(request.POST, instance=query_table_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully')
            return redirect('/vehicles')
    context = {
		'form':form
    }
    return render(request, 'add_vehicle_details.html', context)





def book_list(request):
    books=UploadFileTable1.objects.all()

    return render(request, 'book_list.html',{'books':books})

def upload_book(request):
    books=UploadFileTable1.objects.all()
    if request.method == 'POST':
        form=UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_book')
    else:
        form=UploadBookForm()
    context={"form":form,
             "books":books}
    return render(request, 'upload_book.html',context)


#for practice
def practicepage(request):

    return render(request, 'practice.html')

#for practice
def base1(request):
    title="base"

    return render(request, 'base1.html', {"title":title})

#function for ploting for utils.py

def main_view(request):
    header="Allifmaal Stock Management System "
    query_table_content = Sale.objects.all()#assign all the objects in the table to the variable
    x=[x.item for x in query_table_content]

    y=[y.price for y in query_table_content]

    chart=get_plot(x,y)

    context = {
	"header": header,
    "query_table_content": query_table_content,
    "chart": chart,

	}
    return render(request, 'chart.html',context)


def chartview(request):
    title="Allifmaal Stock Management System "
    query_table_content = AllifmaalStockTable1.objects.all()#assign all the objects in the table to the variable
    context = {#without context, you will not see the form in the page

	    "query_table_content": query_table_content,
     "title": title,
    }
    return render(request,'charts.html',context)

def dashboard_inventory(request):
    title="inventory dashboard"
   

    return render(request,'dashboard_inventory.html')

def staff(request):
    title="inventory dashboard"
   

    return render(request,'staff.html')
def product(request):
    title="inventory dashboard"
   

    return render(request,'product.html')
def order(request):
    title="inventory dashboard"
   

    return render(request,'order.html')

def profile(request):
    title="inventory dashboard"
   

    return render(request,'profile.html')

#below is for contact page
def contact(request):
    title="contact page"
    
    #the form below is normal html form and not django form
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        country=request.POST['country']
        subject=request.POST['subject']
        
        context={
        "firstname":firstname,
        "lastname":lastname,
        "country":country,
        "subject":subject
    }
        
        return render(request,'contact.html',context)
    else:
        context ={
        "title":title,
    }
   

        return render(request,'contact.html',context)


