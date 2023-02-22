import os
import uuid
import datetime
from datetime import timedelta
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from giftproject.settings import EMAIL_HOST_USER

# Create your views here.
def shopreg(request):
    if request.method=='POST':
        a=shopregform(request.POST)
        if a.is_valid():
            sn=a.cleaned_data['name']
            ad=a.cleaned_data['address']
            si=a.cleaned_data['shopid']
            em=a.cleaned_data['email']
            nm=a.cleaned_data['number']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['confirmpassword']
            if ps==cp:
                b=shopregmodel(name=sn,address=ad,shopid=si,email=em,number=nm,password=ps)
                b.save()
                return redirect(shoplog)
            else:
                return HttpResponse("password doesn't match")
    return render(request,'shopregistration.html')

def shoplog(request):
    if request.method=='POST':
        a=shoplogform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            ps=a.cleaned_data['password']
            b=shopregmodel.objects.all()
            request.session['name']=nm
            for i in b:
                if nm==i.name and ps==i.password:
                    request.session['id']=i.id
                    return redirect(profpage)
            else:
                return HttpResponse("login failed")
    return render(request,'shoplogin.html')




def profpage(request):
    name=request.session['name']
    return render(request,'profilepage.html',{'name':name})


def indexpage(request):
    return render(request,'index.html')




def imageupload(request):
    if request.method=='POST':
        a=imageform(request.POST,request.FILES)
        id=request.session['id']
        if a.is_valid():
            im=a.cleaned_data['proname']
            pp=a.cleaned_data['proprice']
            pd=a.cleaned_data['prodes']
            fl=a.cleaned_data['prfile']
            b=imagemodel(shopid=id,proname=im,proprice=pp,prodes=pd,prfile=fl)
            b.save()
            return redirect(prodisplay)
        else:
            return HttpResponse("upload failed")
    return render(request,'fileupload.html')

def prodisplay(request):
    shpid=request.session['id']
    a = imagemodel.objects.all()
    image = []
    name = []
    price=[]
    description=[]
    id=[]
    shopid=[]
    for i in a:
        sid=i.shopid
        shopid.append(sid)
        id1=i.id
        id.append(id1)
        im = i.prfile
        image.append(str(im).split('/')[-1])
        nm = i.proname
        name.append(nm)
        pr=i.proprice
        price.append(pr)
        pd=i.prodes
        description.append(pd)
    mylist=zip(image, name,price,description,id,shopid)
    return render(request, 'prodisplay.html', {'mylist': mylist,'shpid':shpid})


def prodelete(request,id):
    a=imagemodel.objects.get(id=id)
    a.delete()
    return redirect(prodisplay)


def proedit(request,id):
    a=imagemodel.objects.get(id=id)
    im=str(a.prfile).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES): #to check the new file
            if len(a.prfile)>0: #to check old file
                os.remove(a.prfile.path)
            a.prfile=request.FILES['prodimg']
        a.proname=request.POST.get('prodname')
        a.proprice=request.POST.get('prodpri')
        a.prodes = request.POST.get('proddes')
        a.save()
        return redirect(prodisplay)
    return render(request,'editpro.html',{'a':a,'im':im})


def viewallpro(request):
    a = imagemodel.objects.all()
    image = []
    name = []
    price=[]
    description=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        im = i.prfile
        image.append(str(im).split('/')[-1])
        nm = i.proname
        name.append(nm)
        pr=i.proprice
        price.append(pr)
        pd=i.prodes
        description.append(pd)
    mylist=zip(image, name,price,description,id)
    return render(request, 'viewallpro.html', {'mylist': mylist})



def siglog(request):
    return render(request,'signorlog.html')


def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # checking whether the username exist
        #filter() is used to filter ur search and allows u to return only the rows
        # messages.success(): is a framework that allows u to store messages in one request and retreive them in the request page
        # first(): will get first object from filter query
        if User.objects.filter(username=username).first():
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)
        user_obj=User(username=username,first_name=firstname,last_name=lastname,email=email)
        user_obj.set_password(password)
        user_obj.save()
        # uuid module=uuid stands for universally unique identifiers
        # uuid4() creates random uuid
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        # user defined function :send_mail_regis()
        send_mail_regis(email,auth_token) #mail sending function
        return render(request,'success.html')
    return render(request,'userregistration.html')

def uslog(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(uslog)
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified: #if profile object is not in true state
            messages.success(request,'profile is not verified, check your mail')
            return redirect(uslog)
        user=authenticate(username=username,password=password)

        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(uslog)
        return redirect(uspro)
    return render(request,'userlogin.html')

def uspro(request):
    a=request.session['username']
    return render(request,'userprofile.html',{'a':a})
# http://127.0.0.1:8000/gifapp/uspro/
def usl(request):
    return render(request,'userlogandsign.html')

# subject, message, from_email, recipient_list:send_mail
def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    # f: it is a string literal which contains expressions inside curly brackets
    # the expressions are replaced by values
    message=f'click the link to verify your account http://127.0.0.1:8000/gifapp/verify/{auth_token}'
    email_from=EMAIL_HOST_USER #from
    recipient=[email] #to
    # inbuild function :send_mail
    send_mail(subject,message,email_from,recipient)


def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(uslog)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(uslog)
    else:
        messages.success(request,"user not found")
        return redirect(uslog)



def userprodisplay(request):
    a = imagemodel.objects.all()
    image = []
    name = []
    price=[]
    description=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        im = i.prfile
        image.append(str(im).split('/')[-1])
        nm = i.proname
        name.append(nm)
        pr=i.proprice
        price.append(pr)
        pd=i.prodes
        description.append(pd)
    mylist=zip(image, name,price,description,id)
    return render(request, 'userviewpro.html', {'mylist': mylist})


def addcart(request,id):
    uid = request.session['id']
    a=imagemodel.objects.get(id=id)
    if cart.objects.filter(proname=a.proname):
        return HttpResponse("already exist")
    b = cart(useri=uid,proname=a.proname, proprice=a.proprice, prodes=a.prodes, prfile=a.prfile)
    b.save()
    return HttpResponse("product added")
    # return render(request,'userviewpro.html')



def displaycart(request):
    uid = request.session['id']
    a=cart.objects.all()
    image = []
    name = []
    price=[]
    description=[]
    id=[]
    useri = []
    for i in a:
        id1=i.id
        id.append(id1)
        im = i.prfile
        image.append(str(im).split('/')[-1])
        nm = i.proname
        name.append(nm)
        pr=i.proprice
        price.append(pr)
        pd=i.prodes
        description.append(pd)
        ui = i.uid
        useri.append(ui)
    mylist=zip(image, name,price,description,id,useri)
    return render(request, 'cart.html', {'mylist': mylist,'uid':uid})

def wishlistuser(request,id):
    uid = request.session['id']
    a=imagemodel.objects.get(id=id)
    # b=wishlistmodel(proname=a.proname,proprice=a.proprice,prodes=a.prodes,prfile=a.prfile)
    # b.save()
    return HttpResponse("product added")
    return render(request,'userviewpro.html')



def wishtocart(request,id):
    uid = request.session['id']
    a=wishlistmodel.objects.get(id=id)
    if cart.objects.filter(proname=a.proname):
        return HttpResponse("already in wishlist")
    b = cart(useri=uid, proname=a.proname, proprice=a.proprice, prodes=a.prodes, prfile=a.prfile)
    b.save()
    return HttpResponse("product added")


def displaywishlist(request):
    uid=request.session['id']
    a =wishlistmodel.objects.all()
    image = []
    name = []
    price=[]
    description=[]
    id=[]
    useri = []
    for i in a:
        id1=i.id
        id.append(id1)
        im = i.prfile
        image.append(str(im).split('/')[-1])
        nm = i.proname
        name.append(nm)
        pr=i.proprice
        price.append(pr)
        pd=i.prodes
        description.append(pd)
        ui = i.uid
        useri.append(ui)
    mylist=zip(image, name,price,description,id,useri)
    return render(request, 'wishlist.html', {'mylist': mylist,'uid':uid})


def removecart(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(displaycart)

def removewish(request,id):
    a=wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(displaywishlist)

def cartbuy(request,id):
    a=cart.objects.get(id=id)
    im=a.prfile
    x=str(a.prfile).split('/'[-1])
    if request.method=='POST':
        nm=request.POST.get('pronm')
        pr=request.POST.get('propri')
        des=request.POST.get('prode')
        quan=request.POST.get('quantity')
        b=buymodel(pronm=nm,propri=pr,prode=des,quantity=quan)
        total=int(pr)*int(quan)
        return render(request,'finalbill.html',{'tt':total,'nm':nm,'pr':pr,'des':des,'quan':quan})
    return render(request,'buyproduct.html',{'a':a,'im':x})

# http://127.0.0.1:8000/gifapp/cartbuy/5
def bill(request):
    if request.method=='POST':
        a=billforms(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['nam']
            ph=a.cleaned_data['phone']
            em=a.cleaned_data['mail']
            ad=a.cleaned_data['add']
            b=billmodels(nam=nm,phone=ph,mail=em,add=ad)
            return redirect(cardpay)
    return render(request,'finalbill.html')


def cardpay(request):
   if request.method=='POST':
       a=onlinepayform(request.POST)
       if a.is_valid():
            cn=request.POST.get('cardname')
            cnum=request.POST.get('cardnumber')
            ce=request.POST.get('cardexpiry')
            sc=request.POST.get('securitycode')
            b=onlinepaymodel(cardname=cn,cardnumber=cnum,cardexpiry=ce,securitycode=sc)
            return render(request,'buysuccess.html')
       else:
           return HttpResponse("something went wrong")
   return render(request,'cardpayment.html')

def shopnot(request):
    a=shopnotimodel.objects.get(all)
    shopdate=[]
    cont=[]
    for i in a:
        tm=i.shopdate
        shopdate.append(tm)
        ct=i.content
        cont.append(ct)
    s=zip(shopdate,cont)
    return render(request,'shopnot.html')



def usernot(request):
    a=usernotimodel.objects.get(all)
    shopdate=[]
    cont=[]
    for i in a:
        tm=i.shopdate
        shopdate.append(tm)
        ct=i.content
        cont.append(ct)
    s=zip(shopdate,cont)
    return render(request,'usernot.html')
