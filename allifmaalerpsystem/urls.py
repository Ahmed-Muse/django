
from django.urls import path
from . import views
from django.conf import settings#for uploading files
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),# here do not execute index by typing index(), but just point to it by typing index
    path('customers/',views.customers,name='customers'),#the first 'customers' should be html name, second views name, 3rd you can change even
    path('add_customers/',views.add_customers,name='add_customers'),
    path('stock/',views.stock,name='stock'),
    path('add_stock/',views.add_stock,name='add_stock'),
    path('hrm/',views.hrm,name='hrm'),
    path('add_staff/',views.add_staff,name='add_staff'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('eshop/',views.eshop,name='eshop'),
    path('update_customers/<str:pk>/', views.update_customers, name="update_customers"),
    
    path('update_stock/<str:pk>/', views.update_stock, name="update_stock"),
    path('update_staff/<str:pk>/', views.update_staff, name="update_staff"),
    
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),
    
    path('delete_stock/<str:pk>/', views.delete_stock, name="delete_stock"),
    
    path('delete_staff/<str:pk>/', views.delete_staff, name="delete_staff"),
    path('stock_details/<str:pk>/', views.stock_details, name="stock_details"),
    
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    
    path('stock_history/', views.stock_history, name='stock_history'),
    path('delete_history_record/<str:pk>/', views.delete_history_record, name="delete_history_record"),
    path('add_category/', views.add_category, name='add_category'),
    path('calc/', views.calc, name='calc'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('delete_vehicle/<str:pk>/', views.delete_vehicle, name="delete_vehicle"),
    path('update_vehicle_details/<str:pk>/', views.update_vehicle_details, name="update_vehicle_details"),
    
    #path('upload_file/', views.upload_file, name='upload_file'),
    
    path('book_list/', views.book_list, name='book_list'),
    path('upload_book/', views.upload_book, name='upload_book'),
    path('practice/', views.practicepage, name='practice'),
    path('base1/', views.base1, name='base'),
    path('main_view/', views.main_view, name='main_view'),
    path('charts/', views.chartview, name='chartview'),
    path('dashboard_inventory/', views.dashboard_inventory, name='dashboard_inventory'),
    path('staff/', views.staff, name='staff'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('profile/', views.profile, name='profile'),
    
    
    

] 
if settings.DEBUG:#if debug which is in development stage only, then add the path below
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#this will enable django to display the uploaded files
