from django.db import models
from datetime import datetime, date

# Create your models here.

#below is the customers details models/table
class AllifmaalCustomersTable(models.Model):
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_status = models.CharField(max_length=255, blank=True, null=True)
    customer_contacts = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
    		return self.customer_name + ' ' + self.customer_contacts # this will show up in the admin area
	
 
class AllifmaalStockTable1(models.Model):
    part_number = models.CharField(max_length=255, blank=True, null=True)# unique prevents data duplication
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity_in_store = models.IntegerField(blank=False,null=True)
    price = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)#if adding now, pick currrent data and if updating stick to the original date
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    receive_quantity = models.IntegerField(default='0',blank=True,null=True)
    receive_by = models.CharField(max_length=50,blank=True,null=True)
    issue_quantity = models.IntegerField(default='0',blank=True,null=True)
    issue_by = models.CharField(max_length=50,blank=True,null=True)
    issue_to = models.CharField(max_length=50,blank=True,null=True)
    created_by = models.CharField(max_length=50,blank=True,null=True)
    reorder_level = models.IntegerField(default='0',blank=True,null=True)
    
    class meta:
        verbose_name_plural ='Stock data in Allifmaal'#this is what will appear on the admin description
    
    

    
    def __str__(self):
    		return self.part_number + ' ' + self.description # this will show up in the admin area
  


#below is for dynamically creating choice field for gender instead of hardcoding
class AllifmaalHRMTable2Gender(models.Model):
    gender = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.gender
  #Choice field
gender_choice = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
class AllifmaalHRMTable2(models.Model):
    staff_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True,choices=gender_choice)
    title = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    #joined = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)#will add automatically and field
    #will disappear
    #gender = models.ForeignKey(AllifmaalHRMTable2Gender, blank=True, null=True)#got errors
    joined = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    
    def __str__(self):
    		return self.staff_number + ' ' + self.first_name + ' ' + self.last_name# this will show up in the admin area
  
  
  #

#stock history table
class AllifmaalStockHistoryTable(models.Model):
    part_number = models.CharField(max_length=255, blank=True, null=True)# unique prevents data duplication
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity_in_store = models.IntegerField(default='0',blank=True,null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)#if adding now, pick currrent data and if updating stick to the original date
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    receive_quantity = models.IntegerField(default='0',blank=True,null=True)
    receive_by = models.CharField(max_length=50,blank=True,null=True)
    issue_quantity = models.IntegerField(default='0',blank=True,null=True)
    issue_by = models.CharField(max_length=50,blank=True,null=True)
    issue_to = models.CharField(max_length=50,blank=True,null=True)
    created_by = models.CharField(max_length=50,blank=True,null=True)
    reorder_level = models.IntegerField(default='0',blank=True,null=True)
    
    

    
    def __str__(self):
    		return self.part_number + ' ' + self.description # this will show up in the admin area
  
#create category
class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.category_name



#Choice field
primary_meter_options = (
		('Kilometers', 'Kilometers'),
		('Miles', 'Miles'),
	)
vehicle_type_options = (
		('Truck', 'Truck'),
		('Car', 'Car'),
        ('Pickup','Pickup'),
        ('Bus', 'Bus'),
        ('Trailer', 'Trailer'),
        ('Van','Van'),
        ('Tow Truck','Tow Truck'),
        ('Motorcycle','Motorcycle'),
	)
vehicle_status_options = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
class AllifmaalVehiclesTable1(models.Model):
    vehicle_image=models.ImageField(upload_to='books/covers/',null=True, blank=True)
    vehicle_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_make = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    vin = models.CharField(max_length=255, blank=True, null=True)
    starting_odometer = models.IntegerField(default='0',blank=True,null=True)
    primary_meter = models.CharField(max_length=255, blank=True, null=True,choices=primary_meter_options)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True,choices=vehicle_type_options)
    vehicle_status = models.CharField(max_length=255, blank=True, null=True,choices=vehicle_status_options)
    
    
    
    def __str__(self):
    		return self.vehicle_name + ' ' + self.vehicle_make + ' ' + self.vehicle_model# this will show up in the admin area

class UploadFileTable1(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_files=models.FileField(upload_to='books/pdfs/')
    cover=models.ImageField(upload_to='books/covers/',null=True, blank=True)
    
    def __str__(self):
        	return self.title

class Sale(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()
    
    def __str__(self):
        	return (self.item)
    


#THIS IS FOR THE INVOICE SECTIONS
class InvoiceTable(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    customer_name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
    line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    line_three = models.CharField('Line 3', max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)    
    
    line_four = models.CharField('Line 4', max_length=120, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)
    line_five = models.CharField('Line 5', max_length=120, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
			('Receipt', 'Receipt'),
			('Proforma Invoice', 'Proforma Invoice'),
			('Invoice', 'Invoice'),
		)
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __str__(self):
        	return self.customer_name + ' ' + self.line_one +'  '+ str(self.invoice_number)