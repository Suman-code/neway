from abc import ABCMeta
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import FormMixin
from .models import Customer, Cart , Product , OrderPlace
from . forms import LoginForm, MyPasswordChangeForm, UserDetailsForm, UserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import UserDetails
from django.db.models import Q
from django.http import JsonResponse




# Create your views here.

class ProductHome(TemplateView):

    def get(self, request):
        total_item = 0
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='WB')
        trending = Product.objects.filter(category='TND')
        laptop = Product.objects.filter(category='L')
        mobiles = Product.objects.filter(category='M')
        deal_of_the_day = Product.objects.filter(category='DOD')
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))

        return render( request , 'myapp/home.html', {'topwear' : topwear, 'bottomwear' : bottomwear , 'trending' : trending,
        'mobiles' : mobiles , 'laptop' : laptop, 'dealoftheday' : deal_of_the_day , 'totalitem' : total_item})

    

# class for product details
class ProductDetails(View):

    def get(self , request , pk):
        product = Product.objects.get(pk=pk)
        total_item = 0
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product = product.id) & Q( user = request.user)).exists()
            total_item = len(Cart.objects.filter(user=request.user))

        return render (request , 'myapp/productDetails.html' , {'product' : product , 'already_in_cart' : item_already_in_cart, 'totalitem' :total_item})


# add item to cart view
@login_required
def addToCart(request):
    usr = request.user
    product_id = request.GET.get('prod_id')
    productt = Product.objects.get(id=product_id)
    savecart = Cart( user=usr , product = productt)
    savecart.save()

    return redirect('/showcart/')

# show cart view
def showCart(request):
    if request.user.is_authenticated:
        user = request.user
        total_item = 0
        carts = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_charge = 60.0
        total = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==user ]
        if user.is_authenticated:
            total_item = len(Cart.objects.filter(user=user))

        if cart_product:
            for i in cart_product:
                tempamount = (i.quantity * i.product.discounted_price)
                total += tempamount
                total_amount = total + shipping_charge
            return render(request , 'myapp/showcart.html' , {'carts' : carts , 'total_amout' : total_amount , 'total' :total , 'totalitem' : total_item})
        else:
            return render(request , 'myapp/empty.html')




# check out
@login_required
def CheckOut(request):
    user= request.user
    total_item = 0
    adres = UserDetails.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shippingCharge = 70.0
    totalAmount = 0.0
    if user.is_authenticated:
            total_item = len(Cart.objects.filter(user=user))

    cart_product = [p for p in Cart.objects.all()  if  p.user == user]
    if cart_product:
        for i in cart_product:
            tempamount = (i.quantity) * (i.product.discounted_price)
            amount += tempamount
            totalAmount = amount + shippingCharge 
            
    return render (request , 'myapp/checkout.html', {'cart_items' : cart_items, 'adres' : adres , 'totalamount':totalAmount, 'totalitem' : total_item})



#  payment order view
def paymentDone(request):
    if request.method == "GET":
        user = request.user
        addId = request.GET.get('custid')
       
        customerId = UserDetails.objects.get(id=addId)
        cart_item = Cart.objects.filter(user=user)

        for c in cart_item:
            OrderPlace(user=user ,   product = c.product , Customer = customerId, quantity = c.quantity).save()
            c.delete()
    return redirect('/orders/')



# cart order view
@login_required
def cartOrder(request):

    orderplace = OrderPlace.objects.filter(user=request.user)

    return render(request , 'myapp/order.html', {'orderplace' : orderplace})


# sign-up function
class SignUp(View):

    def get(self, request):
        form = UserRegistration()
        
        return render (request , 'myapp/signup.html' , {'form' : form})

    def post(self , request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            messages.success(request , 'Congratulations!! you have registerted successfully. Please login')
            form.save()
            form = UserRegistration()

        return render (request , 'myapp/signup.html' , {'form' : form})



# view buynow

def buyNow(request):

    return render (request , 'myapp/buy.html')


    return render(request , 'myapp/order.html' , {})


# view for mobiles

def mobileView(request , data = None):
    total_item = 0
    user = request.user
    if data == None:
        mobiles = Product.objects.filter(category = 'M')

    elif data == 'apple' or 'samsung' or 'nokia':
        mobiles = Product.objects.filter(category = 'M').filter(brand=data)

   
    if user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))


    return render (request , 'myapp/mobile.html', {'mobiles' : mobiles, 'totalitem' : total_item})


# prifile view

class UserDetailsCls(View):
    
    def get(self, request):
        user = request.user
        userProfile = UserDetails.objects.filter(user=user)
        total_item = 0
        form = UserDetailsForm()
        if user.is_authenticated:
            total_item = len(Cart.objects.filter(user=user))

        return render(request , 'myapp/profile.html' , {'form' : form , 'totalitem' : total_item, 'uProfile' : userProfile })


# chnage Password view
@login_required
def changePasswordView(request):
    if request.method == 'POST':
        user = request.user
        if request.user.is_authenticated:
            total_item = Cart.objects.filter(user=user)
        
            fm = MyPasswordChangeForm(user = request.user , data = request.POST)
            if fm.is_valid():
                messages.success(request , 'You have successfully chnaged your passowrd, please login with your new password')
                fm.save()
            
    else:
        fm = MyPasswordChangeForm(user=request.user)
    return render(request , 'myapp/changepassword.html' , {'form' : fm, 'totalitem' : total_item} )

@login_required
def addressView(request):
    if request.method == 'POST':
    
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            usr = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            locality = form.cleaned_data['email']
            area_and_street = form.cleaned_data['area_and_street']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            landmark = form.cleaned_data['landmark']
            state = form.cleaned_data['state']

            regi = UserDetails(user=usr ,first_name=first_name , last_name= last_name , mobile_number = mobile_number , email = email ,
            locality=locality , area_and_street = area_and_street , city=city , pincode= pincode , landmark= landmark ,state= state)
            regi.save()

            messages.success(request, 'Your new address has been added.')
            form = UserDetailsForm()
            return redirect('/manage-address/')

    else:
        form = UserDetailsForm()
    
    return render(request , 'myapp/address.html' , {'form' : form , 'active' : 'btn-secondary' })


# manage address view
@login_required
def manageAddress(request):
    user= request.user
    total_item = 0
    addres = UserDetails.objects.filter(user=request.user)
    usradd = UserDetails.objects.all()
    if user.is_authenticated:
        total_item = len(Cart.objects.filter(user=user))

    return render (request , 'myapp/manageaddress.html' , { 'addres' : addres , 'usradd' : usradd , 'totalitem' : total_item} )


# update user address
def updateUserAddress(request , id):
    user = request.user
    total_item = 0    
    if request.method == "POST":
        pi = UserDetails.objects.get(pk=id)
        fom = UserDetailsForm(request.POST , instance =pi)
        if fom.is_valid():
            fom.save()
            return HttpResponseRedirect('/manage-address/')
        if user.is_authenticated:
            total_item = len(Cart.objects.filter(user-user))

    else:
        pi = UserDetails.objects.get(pk=id)
        fom = UserDetailsForm(instance=pi)

    return render(request , 'myapp/updateaddress.html' , { 'form' : fom , 'totalitem' : total_item})

# delete the user address
def deleteUserAddress(request , id):
    if request.method == "POST":
        pi = UserDetails.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/manage-address/')
        
    else:
        HttpResponseRedirect('/message-address/')


#plus cart view

def plus_cart(request):
    if request.method == 'GET':
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity += 1
        c.save()
        amount = 0.0
        tempAmount = 0.0
        quantity = 0
        shipping_charge = 70.00
        cart_product = [p for p in Cart.objects.all() if p.user==user ]
        for i in cart_product:
            tempAmount = (i.quantity) * (i.product.discounted_price)
            amount += tempAmount
            

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_charge
            } 
        return JsonResponse(data)


def minusCart(request):
    if request.method == 'GET':
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()

        amount = 0.0
        totalamount = 0.0
        shippingCharge = 70.0

        carts = [p for p in Cart.objects.all() if p.user==user ]

        for i in carts:
            temamount = (i.quantity) * (i.product.discounted_price)
            amount += temamount
           

        data = {
            'quantity' : c.quantity,
            'amount' : amount ,
            'totalamount' : amount + shippingCharge
            
            }

        return JsonResponse(data)


# remove cart view

def removeCart(request):
    total_item = 0
    if request.method ==  "GET":
        user = request.user
        prodId = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prodId) & Q(user=user))
        c.delete()
        
        shipping_charge = 70.0
        amount = 0.0
        totalAmount = 0.0

        product = [p for p in Cart.objects.all() if p.user==user]

        for i in  product:
            temAmount = (i.quantity) * (i.product.discounted_price)
            amount += temAmount

        data = {
            'amount' : amount,
            'totalamount' : amount+shipping_charge}

        return JsonResponse(data)







    






    
