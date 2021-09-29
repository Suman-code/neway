from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator

# Create your models here.

STATE_CHOICES = (
    ('Andra Pradesh', 'Andra Pradesh'),
    ('Arunalchal Pradesh' , 'Arunacahl Pradesh'),
    ('Andaman' , 'Andaman'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('Mumbai' , 'Mumbai'),

    ('Delhi' , 'Delhi'),
    ('Karnataka' , 'KArnataka'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Kerala' , 'Kerala'),
    ('Telengana' , 'Telengana'),
    ('Jharkhand' , 'Jharkhand'),
    ('Gujraj' , 'Gujrrat'),
    ('Maharastra' , 'Maharastara'),
    ('Manipur' , 'Manipur'),
    ('Meghalaya' , 'Meghalaya'),
    ('Nagaland' , 'Nagaland'),
    ('Mizoram' , 'Mizoram'),
    ('Punjab' , 'Punjab'),
    ('J&K' , 'J&K'),
    ('Himachal Pradesh' , 'Hiamchal Pradesh'),
    ('Goa' , 'Goa'),
    ('Tripura', 'Tripura'),
    ('Hariyana' , 'Hariyana')



)

class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 300)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES , max_length = 100)
  

    def __str__(self):
        return str(self.id)

CATAGORY_CHOICES = (
    ('M' , 'Mobile'),
    ('TW' , 'Topwear'),
    ('WB' , 'Bottomwear'),
    ('L' , 'Laptop'),
    ('TND' , 'Trending'),
    ('DOD' , 'deal of the day')


)


class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length = 100)
    category = models.CharField(choices = CATAGORY_CHOICES ,  max_length = 3)
    product_image = models.ImageField(upload_to = 'producting')

    def __str__(self):
        return str(self.id)

   


class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product ,on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On the way' , 'On the way'),
    ('Delivered' , 'Delivered'),
    ('Canceled' , 'Canceled')
)


class UserDetails(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=242)
    locality = models.CharField(max_length = 300)
    area_and_street = models.CharField(max_length=840)
    city = models.CharField(max_length = 100)
    pincode = models.IntegerField()
    landmark = models.CharField(max_length=500)
    state = models.CharField(choices = STATE_CHOICES , max_length = 100)
  

    def __str__(self):
        return str(self.id)



class OrderPlace(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(UserDetails , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_Date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES , default='pending')

   

    @property
    def productPrice(self):
        return self.product.discounted_price  * self.quantity


    





