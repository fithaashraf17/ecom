from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import *
import os

import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
import datetime




# Create your views here.
def index(request):
    query=register_tb.objects.all()
    prd=product_tb.objects.all()

    return render(request,'index.html',{"reg":query,"prd":prd})
def about(request):
    prd=product_tb.objects.all()
    return render(request,'about.html',{"prd":prd})
def coming(request):
    prd=product_tb.objects.all()
    return render(request,'coming.html',{"prd":prd})
def contact(request):
    prd=product_tb.objects.all()

    if request.method=="POST":

        cfname=request.POST["username"]
        cphone=request.POST["phone"]
        cemail=request.POST["email"]
        cmsg=request.POST["message"]
        cpass=request.POST["password"]
        add=contact_tb(name=cfname,phone=cphone,email=cemail,msg=cmsg,password=cpass)
        add.save()

        

        return render(request,'contact.html',{"prd":prd})

    else:
        return  render(request,'contact.html',{"prd":prd})
def login(request):
    if request.method=="POST":
       cname=request.POST["name"]   
       cpass=request.POST["password"]
       print(cpass,"))))))")
       hashpass=hashlib.md5(cpass.encode('utf8')).hexdigest()
       print(hashpass,"*****************")


       log=register_tb.objects.filter(name=cname,hpassword=hashpass)
       if log:
           for x in log:
               request.session["myid"]=x.id
               request.session["name"]=x.name
            #    request.session["img"]=x.image.url


               return render(request,"index.html")
       else:
            return render(request,"login.html",{"msg":"invalid creditionals"})

    else:
        return render(request,"login.html")
def logout(request):
    if request.session.has_key('myid'):
        del request.session["myid"]
        del request.session["name"]
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def register(request):
   if request.method=="POST":
        cname=request.POST["name"]
        cemail=request.POST["email"]
        cphone=request.POST["phone"]
       
        cpass=request.POST["password"]
        hashpass=hashlib.md5(cpass.encode('utf8')).hexdigest()
        print(hashpass,'---')
       

        check=register_tb.objects.filter(name=cname,email=cemail,phone=cphone,password=cpass)
        if check:
            return render(request,"register.html",{'msg':"same"})
        else:
            x = ''.join(random.choices(cname + string.digits, k=8))
            y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            subject = 'welcome to Whats App'
            message = f"Hi {cname}, thank you for registering in Whats App . your user username: {cemail} and  password: {cpass}. Follow https://Wa.me/+18478527243 or https://www.tinder.com.\n Thank You."
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [cemail, ]
            send_mail( subject, message, email_from, recipient_list ) 
            
            add=register_tb(name=cname,email=cemail,phone=cphone,password=cpass,hpassword=hashpass)
            add.save()
            return render(request,"register.html",{'msg':"submitted"})
            

   else:
        return render(request,"register.html")
    
def shop(request):
    prd=product_tb.objects.all()
    return render(request,'shop.html',{"prd":prd})
def single(request):
    if request.session.has_key('myid'):
        ii=request.GET['id']
        prd=product_tb.objects.filter(id=ii)
        return render(request,'single.html',{'prd':prd})

    else:
        return render(request,"login.html")


def productadd(request):
    if request.method=="POST":

        cfname=request.POST["productname"]
        cprice=request.POST["price"]
        cq=request.POST["quantity"]

        cdescription=request.POST["description"]
        print(cdescription,"**************************")

        cimage=request.FILES["image1"]
        check=product_tb.objects.filter(name=cfname)
        if check:
            return render(request,"admin/forms.html",{'msg':"same product added"})
        else:
        
           add=product_tb(name=cfname,price=cprice,image=cimage,description=cdescription,quantity=cq)
           add.save()
        

        return render(request,"admin/indexadmin.html")
    else:
        return render(request,"admin/indexadmin.html")

def delt(request):
    ii=request.GET['id']
    query=register_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/')

def edit(request):
    ii=request.GET['id']
    query=register_tb.objects.filter(id=ii)
    return render (request,"update.html",{'usr':query})
def status(request):
    ii=request.GET['id']
    query=register_tb.objects.filter(id=ii).update(status='approved')
    query1=register_tb.objects.filter(status='pending')
    
    return  render(request,'index.html',{"reg":query1})
def editpro(request):
    ii=request.GET['id']
    query=product_tb.objects.filter(id=ii)
    return render (request,"products.html",{'usr':query})
def deletepro(request):
    ii=request.GET['id']
    query=product_tb.objects.filter(id=ii).delete()
    return HttpResponseRedirect('/')


    
   


def update(request):
   if request.method=="POST":
        cname=request.POST["name"]
        cemail=request.POST["email"]
        cphone=request.POST["phone"]
       
        cpass=request.POST["password"]
        ii=request.GET['id']
        add=register_tb.objects.filter(id=ii).update(name=cname,email=cemail,phone=cphone,password=cpass)
        return HttpResponseRedirect('/')
            

   else:
        return HttpResponseRedirect('/')
def productview(request):
    query=product_tb.objects.all()
    return render(request,'productview.html',{"reg":query})
    



def update_product(request):
    if request.method=="POST":
        up=request.GET['id']
        cfname=request.POST["productname"]
        cprice=request.POST["price"]
        cdescription=request.POST["description"]

        imgup=request.POST['imgupdate']
        if imgup=='Yes':
            image1=request.FILES['image']
            oldrec=product_tb.objects.all().filter(id=up)
            updrec=product_tb.objects.get(id=up)
            for x in oldrec:
                imgurl=x.image.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('Successfully deleted')
                    updrec.image=image1
                    updrec.save()
        product_tb.objects.filter(id=up).update(name=cfname,price=cprice,description=cdescription)
        return HttpResponseRedirect('/productview/')
    else:
        return HttpResponseRedirect('/productview/')
def blocks(request):
     return render(request,"admin/blocks.html")
def cards(request):
     return render(request,"admin/cards.html")
def carousels(request):
     return render(request,"admin/carousels.html")
def forms(request):
    query=product_tb.objects.all()
    query1=register_tb.objects.all()
    # return render(request,'index.html',{"reg1":query1})
    return render(request,"admin/forms.html",{"reg":query,"reg1":query1})
    

def statuspro(request):
    ii=request.GET['id']
    query=product_tb.objects.filter(id=ii).update(status='approved')
    query1=product_tb.objects.filter(status='pending')
    return  render(request,'index.html',{"reg":query1})
    
def indexadmin(request):
     return render(request,"admin/indexadmin.html")
def people(request):
     return render(request,"admin/people.html")
def pricing(request):
     return render(request,"admin/pricing.html")



def product_addcart(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			pids=request.GET['id']
			petdet=product_tb.objects.all().filter(id=pids)
			for x in petdet:
				unitprice=x.price
			qty=request.POST['qty']
			shipping=int(int(unitprice)*10/100)
			total=int(unitprice)*int(qty)+shipping
			date= datetime.datetime.now()
			ii=request.session["myid"]
			print(ii)				
			uid=register_tb.objects.get(id=ii)
			x = datetime.datetime.now()
			pid=product_tb.objects.get(id=pids)
			ii=register_tb.objects.get(id=ii)
			check=cart_tb.objects.all().filter(user_id=ii,product_id=pids,price=unitprice,total=total,date=date)
			if check:
				mypet=cart_tb.objects.all().filter(user_id=ii,status='pending')
				return render(request,'cart.html',{'uv':mypet,'msgkey':'Already Add to cart'})
			else:
				tocart=cart_tb(user_id=ii,product_id=pid,price=unitprice,total=total,date=date,quantity=qty)
				tocart.save()
				thispet=product_tb.objects.all().filter(id=pids)
				for x in thispet:
					oldqty=x.quantity
				newqty=int(oldqty)-int(qty)
				product_tb.objects.all().filter(id=pids).update(quantity=newqty)
				mycart=cart_tb.objects.all().filter(user_id=ii,status='pending')
				grandtotal=0
				for x in mycart:
					grandtotal=int(x.total)+grandtotal
				mypet=cart_tb.objects.all().filter(user_id=ii,status='pending')
				return render(request,'cart.html',{'uv':mypet,'gt':grandtotal,'msgkey':'Add to cart'})
	else:
		print("*************************************************************")
		return render(request,'login.html')
    
    
# def cart(request):
#     query=cart_tb.objects.all()
#     return render(request,'cart.html',{"uv":query})
    


  
def cart(request):
	if request.session.has_key('myid'):
		ii=request.session['myid']
		mycart=cart_tb.objects.all().filter(user_id=ii,status='pending')
		grandtotal=0
		for x in mycart:
			grandtotal=int(x.total)+grandtotal
		mypet=cart_tb.objects.all().filter(user_id=ii,status='pending')
		return render(request,'cart.html',{'uv':mypet,'gt':grandtotal})
	else:
		return render(request,'login.html')


def delete_cartitem(request):
    ii=request.session['myid']
    cid=request.GET['id']
    cartitem=cart_tb.objects.all().filter(id=cid)
    for x in cartitem:
        itemid=x.product_id.id
        quantity=x.quantity
    petsdata=product_tb.objects.all().filter(id=itemid)
    for x in petsdata:
        oldqty=x.quantity
    newqty=int(oldqty)+int(quantity)
    product_tb.objects.all().filter(id=itemid).update(quantity=newqty)
    cart_tb.objects.all().filter(id=cid).delete()
    mycart=cart_tb.objects.all().filter(user_id=ii,status='pending')
    grandtotal=0
    for x in mycart:
        grandtotal=int(x.total)+grandtotal
    mypet=cart_tb.objects.all().filter(user_id=ii,status='pending')
    return render(request,'cart.html',{'uv':mypet,'gt':grandtotal,'msg':'Successfully deleted'})
def payment(request):
    if request.session.has_key('myid'):
        gt=request.GET['gt']
        if request.method=='GET':
            pid=request.GET.get('id')
            ii=request.session['myid']
            prdview=product_tb.objects.filter(id=pid)
            usrview=register_tb.objects.filter(id=ii)
            print(pid,"***********************")
            return render(request,"payment/index.html",{"prd":prdview,"usr":usrview,"amount":gt})
    else:
        return render(request,'login.html')

def  clearcart(request):
       ii=request.session['myid']

       cart_tb.objects.all().filter(user_id=ii,status="pending").delete()
       return HttpResponseRedirect('/')



    


def makepayments(request):
    if request.method=="POST":
        uid=request.POST['userid']
        ii=register_tb.objects.get(id=uid)
        amount=request.POST['amount']
        # print
        x = datetime.datetime.now()
        check=payment_tb.objects.filter(user_id=ii,amount=amount,date=x)
        if check:
            return HttpResponseRedirect('/cart/')
        else:
            cart_tb.objects.filter(user_id=ii).update(status="paid")
            add= payment_tb(user_id=ii,amount=amount,date=x,status="paid")
            add.save()
           
            return HttpResponseRedirect('/')

def search(request):
    if request.method=="GET":

        srh=request.GET['q']
        searchitem=product_tb.objects.filter(name=srh)
        for x in searchitem:
            itemid=x.id
        print(srh,'ppppp')
        item=product_tb.objects.filter(id=itemid)
        return render(request,'single.html',{'prd':item})
    else:
        return HttpResponseRedirect('/')


def subcribe(request):
    if request.method=="POST":

        mail=request.POST['email']
        x = datetime.datetime.now()
        item=email_tb(email=mail,date=x)
        item.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def userdetail(request):

 if request.session.has_key('myid'):
    ii=request.session['myid']
    query=register_tb.objects.filter(id=ii)
    return render (request,"userdetail.html",{'usr':query})
 else:
       return HttpResponseRedirect('/')

def changepass(request):
    ii=request.session['myid']
    query=register_tb.objects.filter(id=ii)

    if request.method=="POST":
        oldpass=request.POST['oldpass']
        newpass=request.POST['newpass']
        check=register_tb.objects.filter(id=ii)
        for x in check:
            password=x.password
        if password == oldpass:
            hashpass=hashlib.md5(newpass.encode('utf8')).hexdigest()

            register_tb.objects.filter(id=ii).update(password=newpass,hpassword=hashpass)
            return HttpResponseRedirect('/logout/')
        else:
            return render (request,"changepass.html",{'usr':query,"msg": "invalid"})       
        
    else:
        return render (request,"changepass.html",{'usr':query})


def forgotpass(request):
    if request.method=="POST":
        email=request.POST['email']
        check=register_tb.objects.filter(email=email)
        if check:
            return render (request,"passchange.html",{'usr':check})
        else:
            return render (request,"forgotpassword.html",{"msg": "invalid"})

    else:
        return render (request,"forgotpassword.html")

def forgotpasschange(request):
    if request.method=="POST":
        uid=request.POST['uid']
        passw=request.POST['pass']
        conpass=request.POST['conpass']
        usr=register_tb.objects.filter(id=uid)
        if passw == conpass:
            hashpass=hashlib.md5(passw.encode('utf8')).hexdigest()
            register_tb.objects.filter(id=uid).update(password=passw,hpassword=hashpass)
            return HttpResponseRedirect('/')


        else:
            return render (request,"passchange.html",{"msg": "invalid",'usr':usr})

    else:   
        uid=request.GET['uid']
        usr=register_tb.objects.filter(id=uid)

        return render (request,"passchange.html",{'usr':usr})