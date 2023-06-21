from django.contrib import admin

# Register your models here.

from.models import Vendor

class vendorAdmin(admin.ModelAdmin):
    list_display= ("name","amount","contacts","location","password","date_created")

admin.site.register(Vendor,vendorAdmin)