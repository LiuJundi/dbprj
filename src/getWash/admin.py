from django.contrib import admin
from .models import *
#from .forms import *

class ClothAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "unitPrice"]

admin.site.register(Cloth, ClothAdmin)

class ClothDetailAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]

admin.site.register(ClothDetail, ClothDetailAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "sumPrice"]

admin.site.register(Order, OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "firstName", "lastName"]

admin.site.register(Customer, CustomerAdmin)

class AddressAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "school", "building"]
	
admin.site.register(Address, AddressAdmin)
