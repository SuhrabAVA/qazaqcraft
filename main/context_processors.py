from .models import Contact

def contact_data(request):
    try:
        contact = Contact.objects.first()
    except Contact.DoesNotExist:
        contact = None
    return {'contact': contact}
