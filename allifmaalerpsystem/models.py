from django.db import models

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
	
 
class AllifmaalStockTable(models.Model):
    part_number = models.CharField(max_length=255, blank=True, null=True)# unique prevents data duplication
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity_in_store = models.IntegerField(default='0',blank=True,null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
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
    
    

    
    def __str__(self):
    		return self.part_number + ' ' + self.description # this will show up in the admin area
  
  
  #Choice field
gender_choice = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
class AllifmaalHRMTable(models.Model):
    staff_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True,choices=gender_choice)
    title = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    joined = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __str__(self):
    		return self.staff_number + ' ' + self.first_name + ' ' + self.last_name# this will show up in the admin area
  
  
  

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