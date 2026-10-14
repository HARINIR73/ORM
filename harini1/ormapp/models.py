from django.db import models
from django.contrib import admin
class myorder(models.Model):
    s_no=models.IntegerField(primary_key=True)
    order_id=models.IntegerField()
    date=models.DateField()
    category=models.CharField(max_length=10)
    quantity=models.IntegerField()
    price=models.IntegerField()
    paymentmethod=models.CharField(max_length=10)
class myorderAdmin(admin.ModelAdmin):
    list_display=["s_no","order_id","date","category","quantity","price","paymentmethod"]

# Create your models here.
