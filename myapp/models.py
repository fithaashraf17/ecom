from django.db import models

# from proj4.myapp.views import status

# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200,default="")
    password=models.TextField(default="")
    hpassword=models.TextField(default="")

    status=models.CharField(max_length=200,default="pending")

class contact_tb(models.Model):
    name=models.CharField(max_length=200,default="")
    # phone=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200,default="")
    # password=models.TextField(default="")

    msg=models.TextField(default="")
class product_tb(models.Model):
    name=models.CharField(max_length=200,default="")
    description=models.CharField(max_length=200,default="")
    price=models.CharField(max_length=200,default="")
    image=models.FileField(upload_to="product" )
    quantity=models.CharField(max_length=200,default="")


    status=models.CharField(max_length=200,default="pending")
class admin_tb(models.Model):
    name=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200,default="")
    passsword=models.TextField(default="")
class cart_tb(models.Model):
    product_id=models.ForeignKey(product_tb, on_delete=models.CASCADE)
    user_id=models.ForeignKey(register_tb, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=200,default="")
    price=models.CharField(max_length=200,default="")
    total=models.CharField(max_length=200,default="")
    date=models.CharField(max_length=200,default="")

    status=models.CharField(max_length=200,default="pending")
class payment_tb(models.Model):
    user_id=models.ForeignKey(register_tb, on_delete=models.CASCADE)
    
    date=models.CharField(max_length=200,default="")
   
    amount=models.CharField(max_length=200,default="")
    
    status=models.CharField(max_length=200,default="pending")
class email_tb(models.Model):
    email=models.CharField(max_length=200,default="")
    date=models.CharField(max_length=200,default="")


   