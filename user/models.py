from tkinter import CASCADE
from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Usermaster'
        
    
class Customer(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to ="customer_img")
    class Meta:
        db_table = 'Customer'
    
    
class Housekeeper(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to ="housekeeper_img")
    class Meta:
        db_table = 'Housekeeper'
    