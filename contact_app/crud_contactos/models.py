# third parties
from django.db import models
from django.db.models.fields import IntegerField, CharField, EmailField


class CrudContacts(models.Model):    
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    company = CharField(max_length=100)
    job_title = CharField(max_length=50)
    phone = CharField(max_length=12)
    email = EmailField(max_length=100)
    cel_phone = CharField(max_length=12)
    note = CharField(max_length=250)

    def __str__(self) -> str:
        return f'<Contact: "{self.first_name}, {self.last_name}">'
