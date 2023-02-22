from django import forms


class shopregform(forms.Form):
    name=forms.CharField(max_length=30)
    address=forms.CharField(max_length=30)
    shopid=forms.IntegerField()
    email=forms.EmailField()
    number=forms.IntegerField()
    password=forms.CharField(max_length=30)
    confirmpassword=forms.CharField(max_length=30)

class shoplogform(forms.Form):
    name=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)



class imageform(forms.Form):
    proname=forms.CharField(max_length=30)
    proprice=forms.IntegerField()
    prodes=forms.CharField(max_length=30)
    prfile=forms.ImageField()


class billforms(forms.Form):
    nam=forms.CharField(max_length=30)
    phone=forms.IntegerField()
    mail=forms.EmailField()
    add=forms.CharField(max_length=50)

class onlinepayform(forms.Form):
    cardname=forms.CharField(max_length=40)
    cardnumber=forms.CharField(max_length=40)
    cardexpiry=forms.CharField(max_length=40)
    securitycode=forms.CharField(max_length=40)