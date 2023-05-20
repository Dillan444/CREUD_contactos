# third parties
from django.urls import path

# local
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new_contact", views.new_contact, name="new_contact"),
    path("contact_update/<int:contact_id>", views.contact_update, name="contact_update"),
    path("contact_delete/<int:contact_id>", views.contact_delete, name="contact_delete"),
    path("contact_detail/<int:contact_id>", views.contact_detail, name="contact_detail")
]
