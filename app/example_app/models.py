from django.db import models


class TelUser(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=255)
    language = models.CharField(max_length=255, default='uz')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

class Customer(models.Model):
    tg_user = models.OneToOneField(TelUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class ConfirmChannel(models.Model):
    name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Model(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='product_media/')
    text = models.TextField(default='')

    def __str__(self):
        return self.name

class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_media')
    image = models.ImageField(upload_to='product_media/')