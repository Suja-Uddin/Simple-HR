from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class User(models.Model):
    user_types = (
        ('1', 'NORMAL'),
        ('2', 'HR'),
        ('3', 'MANAGER')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    type = models.CharField(max_length=100, choices=user_types, default= '1')
    is_logged_in = models.BooleanField(default=False)


class Request(models.Model):
    statuses = (
        ('1', 'Open'),
        ('2', 'HR Reviewed'),
        ('3', 'Processed')
    )
    details = models.CharField(max_length=255)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_requester_id')
    processor = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null=True, related_name= '%(class)s_request_processor_id')
    status = models.CharField(max_length=20, choices=statuses, default='1')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
    def clean_email(self):
        print("email cleaning")
        email = self.cleaned_data['email']
        if email[email.index('@')+1:] != 'misfit.tech':
            print(email[email.index('@')+1:])
            raise ValidationError(_('Not a valid MISFIT email'))
        return email