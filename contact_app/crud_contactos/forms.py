# third parties
from django import forms


class CreateContact(forms.Form):
    first_name = forms.CharField(
        label='Nombre',
        max_length=50,
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=50,
    )
    company = forms.CharField(
        label='Empresa',
        max_length=100,
    )
    job_title = forms.CharField(
        label='Puesto de trabajo',
        max_length=50,
    )
    phone = forms.CharField(
        label='Telefono fijo',
        max_length=15,
    )
    email = forms.EmailField(
        label='Correo',
        max_length=100,
    )
    cel_phone = forms.CharField(
        label='Celular',
        max_length=15,
    )
    note = forms.CharField(
        label='Nota',
        max_length=250,
    )