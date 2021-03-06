"""allifmaalems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path, include
from allifmaalerpsystem import views
from django.conf import settings#for uploading files
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
     path('',include('allifmaalerpsystem.urls')), #to point the root URLconf at the polls.urls module
     path('customers/',include('allifmaalerpsystem.urls')),
     path('add_customers/',include('allifmaalerpsystem.urls')),
     path('stock/',include('allifmaalerpsystem.urls')),
     path('add_stock/',include('allifmaalerpsystem.urls')),
     path('hrm/',include('allifmaalerpsystem.urls')),
     path('add_staff/',include('allifmaalerpsystem.urls')),
     path('dashboard/',include('allifmaalerpsystem.urls')),
     path('eshop/',include('allifmaalerpsystem.urls')),
     path('update_customers/',include('allifmaalerpsystem.urls')),
     
     path('update_stock/',include('allifmaalerpsystem.urls')),
     path('update_staff/',include('allifmaalerpsystem.urls')),
     path('delete_customer/',include('allifmaalerpsystem.urls')),
     path('delete_stock/',include('allifmaalerpsystem.urls')),
     path('delete_staff/',include('allifmaalerpsystem.urls')),
     path('stock_details/',include('allifmaalerpsystem.urls')),
     path('issue_items/',include('allifmaalerpsystem.urls')),
     path('receive_items/',include('allifmaalerpsystem.urls')),
     path('reorder_level/',include('allifmaalerpsystem.urls')),
     path('accounts/', include('registration.backends.default.urls')),
     path('stock_history/', include('registration.backends.default.urls')),
     path('delete_history_record/', include('registration.backends.default.urls')),
     path('add_category/', include('registration.backends.default.urls')),
     path('calc/', include('registration.backends.default.urls')),
     path('vehicles/', include('registration.backends.default.urls')),
     path('delete_vehicle/',include('allifmaalerpsystem.urls')),
     path('update_vehicle_details/',include('allifmaalerpsystem.urls')),
     #path('upload_file/',include('allifmaalerpsystem.urls')),
     
     path('upload_book/',include('allifmaalerpsystem.urls')),
     path('book_list/',include('allifmaalerpsystem.urls')),
     path('practice/',include('allifmaalerpsystem.urls')),
     path('base1/',include('allifmaalerpsystem.urls')),
     path('charts/',include('allifmaalerpsystem.urls')),
     path('dashboard_inventory/',include('allifmaalerpsystem.urls')),
     path('staff/',include('allifmaalerpsystem.urls')),
     path('product/',include('allifmaalerpsystem.urls')),
     path('order/',include('allifmaalerpsystem.urls')),
     path('profile/',include('allifmaalerpsystem.urls')),
     path('contact/',include('allifmaalerpsystem.urls')),
     
     path('dailytimesheet/',include('allifmaalerpsystem.urls')),
     path('dailymileage/',include('allifmaalerpsystem.urls')),
     path('fillups/',include('allifmaalerpsystem.urls')),
     path('services/',include('allifmaalerpsystem.urls')),
     path('expenses/',include('allifmaalerpsystem.urls')),
     path('reminders/',include('allifmaalerpsystem.urls')),
     
    
      
]
#if settings.DEBUG:#if debug which is in development stage only, then add the path below
    #urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#