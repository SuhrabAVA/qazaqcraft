from django.contrib import admin
from .models import CatalogCategory, About, Work, Contact, Category, CatalogItem, PhoneNumber, Email, Request

from django.utils.text import slugify 

admin.site.register(CatalogCategory)
admin.site.register(About)
admin.site.register(Work)

admin.site.register(CatalogItem)
admin.site.register(Category)
class PhoneInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneInline, EmailInline]

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)

# main/admin.py



@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at',)
