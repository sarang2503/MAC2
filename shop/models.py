from django.db import models
import datetime
class Product(models.Model):
    product_id = models.AutoField
#    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product_name = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=30, default="")
    subcategory = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300,default="")
    pub_date = models.DateField(("Date"), default=datetime.date.today)
    image = models.ImageField(upload_to="shop/images",default="")


