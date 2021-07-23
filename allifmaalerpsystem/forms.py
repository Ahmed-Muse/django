from django import forms#we import this so that we use the inbuilt forms module of django
from .models import *

############### START OF CUSTOMERS#######################
class CustomerCreateForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = AllifmaalCustomersTable
        text_fields = ['customer_name', 'project_name', 'project_status',
                        'customer_contacts','contact_person','customer_address']
        fields='__all__'# this was used because of an error when running and the error said " .ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form CustomerCreateForm needs updating.

class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = AllifmaalCustomersTable
        fields = ['customer_name','project_name']#you can not change the name of this variable
            
            
class AddStockForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = AllifmaalStockTable
        text_fields = ['part_number', 'description', 'quantity_in_store','price','comments']
        fields='__all__'# this was used because of an error when running and the error said " .ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form CustomerCreateForm needs updating.


    #start of customized form validation functions..............................
        #the function has to be a child of of the above class
    def clean_part_number(self):# THIS FUNCTION HAS TO BE NAME AS THE FIELD IT VALIDATES PRECEEDED BY CLEAN
        part_number = self.cleaned_data.get('part_number')
        if not part_number:
            raise forms.ValidationError('This field is required')
        
        #start of section to avoid duplications
        for instance in AllifmaalStockTable.objects.all():
            if instance.part_number==part_number:
                raise forms.ValidationError(" The part number "+ part_number +' already exists in the system')
        # end of section to avoid duplications
        
        return part_number
    
    
    #end of customized form validation functions..............................
    
    
class StockSearchForm(forms.ModelForm):
    csv = forms.BooleanField(required=False)# This is for exporting to data in CSV format
    class Meta:
        model = AllifmaalStockTable
        fields = ['part_number','description']
    
class AddStaffForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = AllifmaalHRMTable
        text_fields = ['staff_number', 'first_name', 'middle_name','last_name','gender','title','department','joined']
        fields='__all__'# this was used because of an error when running and the error said " .
        
    #start of customized form validation functions to avoid adding empty fields..............................
        #the function has to be a child of of the above class
    def clean_staff_number(self):# THIS FUNCTION HAS TO BE NAME AS THE FIELD IT VALIDATES PRECEEDED BY CLEAN
        staff_number = self.cleaned_data.get('staff_number')
        if not staff_number:
            raise forms.ValidationError('This field is required')
        
        #start of section to avoid duplications
        for instance in AllifmaalHRMTable.objects.all():
            if instance.staff_number==staff_number:
                raise forms.ValidationError(" The staff number "+ staff_number +' already exists in the system')
        # end of section to avoid duplications
        
        return staff_number
    
    
    #end of customized form validation functions..............................        

class StaffSearchForm(forms.ModelForm):
    class Meta:
        model = AllifmaalHRMTable
        fields = ['staff_number','first_name']



# UPDATE SECTIONS
#customer update form
class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = AllifmaalCustomersTable
        fields = ['customer_name', 'project_name', 'project_status','customer_contacts','contact_person','customer_address']
        fields='__all__'
    
#stock update form
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = AllifmaalStockTable
    
        fields = ['part_number', 'description', 'quantity_in_store','price','comments']
        fields='__all__'   

#staff update form		
class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = AllifmaalHRMTable
    
        fields = ['staff_number', 'first_name', 'middle_name','last_name','gender','title','department','joined']
        fields='__all__'
        
        
#forms to receive and issue requests
class IssueItemForm(forms.ModelForm):
    	class Meta:
            model = AllifmaalStockTable
            fields = ['issue_quantity', 'issue_to']


class ReceiveItemForm(forms.ModelForm):
	class Meta:
		model = AllifmaalStockTable
		fields = ['receive_quantity']


#reorder level form
class StockReorderLevelForm(forms.ModelForm):
    class Meta:
        model=AllifmaalStockTable
        fields =['reorder_level']
        
#Form for stock history StaffSearchForm
class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = AllifmaalStockHistoryTable
        fields = ['part_number', 'description', 'start_date', 'end_date']
        

#form to create category
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class AddVehicleDetailsForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = AllifmaalVehiclesTable1
        text_fields = ['vehicle_image','vehicle_name', 'vehicle_make', 'vehicle_model',
                       'year','license','vin','starting_odometer','primary_meter','vehicle_type','vehicle_status']
        fields='__all__'# this was used because of an error when running and the error said " .
        

class VehicleDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = AllifmaalVehiclesTable1
        fields = ['vehicle_image','vehicle_name', 'vehicle_make', 'vehicle_model',
                       'year','license','vin','starting_odometer','primary_meter','vehicle_type','vehicle_status']
        fields='__all__'

#form to upload files
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
class UploadBookForm(forms.ModelForm):
    class Meta:
        model = UploadFileTable1
        fields = ['title', 'author', 'image_file','cover']
        fields='__all__'