from django.db import models

class CatalogCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='catalog_categories/')

    def __str__(self):
        return self.name
    
class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "О компании"
    
class Work(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    address = models.CharField(max_length=255, blank=True)
    map_embed = models.TextField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, related_name='phones', on_delete=models.CASCADE)
    number = models.CharField(max_length=30)

class Email(models.Model):
    contact = models.ForeignKey(Contact, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField()



    
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class CatalogItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50, blank=True) 
    size = models.CharField(max_length=50, blank=True) 
    image = models.ImageField(upload_to='catalog/', blank=True, null=True)  

    def __str__(self):
        return self.name
# main/models.py


class Request(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    message = models.TextField(blank=True, null=True, verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
