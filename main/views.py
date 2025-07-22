from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Category, CatalogItem, Contact, Work
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Request
def index(request):
    categories = Category.objects.all()
    works = Work.objects.all()
    contact = Contact.objects.first()
    return render(request, 'index.html', {
        'categories': categories,
        'works': works,
        'contact': contact
    })

def some_view(request):

    contact = Contact.objects.filter() # или filter().last()
    return render(request, 'your_template.html', {'contact': contact})

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'categories': categories})

def works_view(request):
    works = Work.objects.all()
    return render(request, 'your_template.html', {'works': works})
def home(request):
    works = Work.objects.all()
    return render(request, 'index.html', {'works': works})
def exact_catalog(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = CatalogItem.objects.filter(category=category)
    return render(request, 'exact_catalog.html', {
        'category': category,
        'items': items
    })

@csrf_exempt
# main/views.py



def request_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Request.objects.create(name=name, phone=phone, message=message)

        return redirect('index')  

    return render(request, 'request.html')
