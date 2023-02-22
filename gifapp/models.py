from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class shopregmodel(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    shopid=models.IntegerField()
    email=models.EmailField()
    number=models.IntegerField()
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class imagemodel(models.Model):
    shopid=models.IntegerField()
    proname=models.CharField(max_length=30)
    proprice=models.IntegerField()
    prodes=models.CharField(max_length=30)
    prfile=models.ImageField(upload_to='gifapp/static')
    def __str__(self):
        return self.proname


class cart(models.Model):
    uid = models.IntegerField()
    proname = models.CharField(max_length=30)
    proprice = models.IntegerField()
    prodes = models.CharField(max_length=30)
    prfile = models.ImageField()
    def __str__(self):
        return self.proprice

class wishlistmodel(models.Model):
    uid=models.IntegerField()
    proname = models.CharField(max_length=30)
    proprice = models.IntegerField()
    prodes = models.CharField(max_length=30)
    prfile = models.ImageField()
    def __str__(self):
        return self.prodes

class buymodel(models.Model):
    pronm = models.CharField(max_length=30)
    propri=models.IntegerField()
    prode= models.CharField(max_length=30)
    prfl = models.ImageField()
    quantity=models.IntegerField()


class billmodels(models.Model):
    nam=models.CharField(max_length=30)
    phone=models.IntegerField()
    mail=models.EmailField()
    add=models.CharField(max_length=50)
    total = models.IntegerField()

class onlinepaymodel(models.Model):
    cardname=models.CharField(max_length=40)
    cardnumber=models.CharField(max_length=40)
    cardexpiry=models.CharField(max_length=40)
    securitycode=models.CharField(max_length=40)
    def __str__(self):
        return self.cardname


class shopnotimodel(models.Model):
    content=models.CharField(max_length=200)
    shopdate=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content

class usernotimodel(models.Model):
    content=models.CharField(max_length=200)
    userdate=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content