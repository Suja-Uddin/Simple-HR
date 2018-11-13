from django.db import models


class User(models.Model):
    user_types = (
        (1, 'NORMAL'),
        (2, 'HR'),
        (3, 'MANAGER')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    type = models.CharField(max_length=100, choices=user_types, default= 1)

class Request(models.Model):
    details = models.CharField(max_length=255)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name= '%(class)s_requester_id')
    processor = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null=True, related_name= '%(class)s_request_processor_id')
