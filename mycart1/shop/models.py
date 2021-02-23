from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=40)
    category = models.CharField(max_length=50,default='')
    subcategory = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default='')
    desc = models.CharField(max_length=100)
    publish_date = models.DateField()

    # product_name=,category=,subcategory=,price=,desc=
    def __str__(self):
        return self.product_name

