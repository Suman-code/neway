from collections import namedtuple
from myapp.forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, SetMyPassword
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('' , views.ProductHome.as_view (), name='home'),
    path('product-detail/<int:pk>/' , views.ProductDetails.as_view() , name="product-detail"),

    path('add-to-cart/' , views.addToCart , name="add-to-cart"),
    path('showcart/' , views.showCart, name="showcart"),
    path('buynow/' , views.buyNow , name="buy_now"),
    path('checkout/' , views.CheckOut , name="checkout"),

    # authentication urls
    path('accounts/login/' , auth_views.LoginView.as_view(template_name = 'myapp/login.html' , authentication_form =  LoginForm), name = "login" ),
    path('logout/' , auth_views.LogoutView.as_view(next_page = 'login') , name="logout"),
    path('chnagepassword/' , views.changePasswordView, name = "changepassword"),
    path('signup/' ,  views.SignUp.as_view(), name="signup"),
    path('passowrd-reset', auth_views.PasswordResetView.as_view(template_name = 'myapp/password-reset.html', form_class = MyPasswordResetForm), name="reset-password"),
    path('password-reset/done/' ,auth_views.PasswordResetDoneView.as_view(template_name = 'myapp/password-reset-done.html') , name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/' ,auth_views.PasswordResetConfirmView.as_view(template_name = 'myapp/password-reset-confirm.html' , form_class = SetMyPassword) , name="password_reset_confirm"),
    path('password-reset-complete/' ,auth_views.PasswordResetCompleteView.as_view(template_name = 'myapp/password-reset-complete.html') , name="password_reset_complete"),
   
    path('buy' , views.buyNow , name="buy"),
    path('mobiles/' , views.mobileView , name="mobiles"),
     path('mobiles/<slug:data>' , views.mobileView , name="mobiledata"),
    #path('profile/' , views.profileView , name='profile'),
    path('profile/' , views.UserDetailsCls.as_view() , name="profile"),
    path('addaddress/' , views.addressView, name="add-address"),
    path('manage-address/' , views.manageAddress, name="manage-address"),
    path('update/user/address/<int:id>/' , views.updateUserAddress, name="update-user-address"),
    path('delete/user/addres/<int:id>/' , views.deleteUserAddress , name="delete-user-address"),
    path('pluscart/' , views.plus_cart),
    path('minuscart/' , views.minusCart),
    path('removecart/' , views.removeCart),
    path('orders/' , views.cartOrder , name="orders"),
    path('paymentdone/' , views.paymentDone)



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)