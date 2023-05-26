# third parties
from django.shortcuts import render, redirect

# local
from crud_contactos.models import CrudContacts
from crud_contactos.forms import CreateContact

def index(request):
    query_contacts = CrudContacts.objects.all()

    context = {
        'show_contacts': query_contacts
    }
    return render(request, 'home.html', context)


def new_contact(request):
    create_contact = CreateContact()

    context = {
        'create_contact': create_contact
    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company = request.POST['company']
        job_title = request.POST['job_title']
        phone = request.POST['phone']
        email = request.POST['email']
        cel_phone = request.POST['cel_phone']
        note = request.POST['note']

        new_contact = CrudContacts(
            first_name = first_name,
            last_name = last_name,
            company = company,
            job_title = job_title,
            phone = phone,
            email = email,
            cel_phone = cel_phone,
            note = note,
        )
        new_contact.save()
        redirect('/')
            
    return render(request, "new_contact.html", context)


def contact_update(request, contact_id):
    return render(request, "contact_update.html", {"contact_id": contact_id})


def contact_delete(request, contact_id):
    return render(request, "contact_delate.html", {"contact_id": contact_id})


def contact_detail(request, contact_id):
    return render(request, "contact_detail.html", {"contact_id": contact_id})

