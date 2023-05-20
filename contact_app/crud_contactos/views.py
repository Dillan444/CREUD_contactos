# third parties
from django.shortcuts import render
from django.http import HttpResponse

# local


def index(request):
    return render(request, 'home.html')
<<<<<<< HEAD


def new_contact(request):
    return render(request, "new_contact.html")


def contact_update(request, contact_id):
    return render(request, "contact_update.html", {"contact_id": contact_id})


def contact_delete(request, contact_id):
    return render(request, "contact_delate.html", {"contact_id": contact_id})


def contact_detail(request, contact_id):
    return render(request, "contact_detail.html", {"contact_id": contact_id})
=======
>>>>>>> db_model
