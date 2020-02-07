from django import forms

from landing.contact_form import models


class ContactForm(forms.ModelForm):
    """
    Contact form.
    """

    class Meta:
        model = models.ContactForm
        fields = ('name', 'phone_number', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'Введите имя...'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control mb-30 phone-input',
                'placeholder': 'Введите номер...'}
            ),
            'message': forms.Textarea(attrs={
                'class': 'form-text-area mb-30', 'cols': 30, 'rows': 6, 'placeholder': 'Сообщение*'
                }
            ),
        }