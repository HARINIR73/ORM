from django.contrib import admin
from .models import myorder,myorderAdmin
class myorderAdmin(admin.ModelAdmin):
    list_display=["s_no","order_id","date","category","quantity","price","paymentmethod"]
admin.site.register(myorder,myorderAdmin)

# Register your models here.
