from django.conf import settings
from django.db import models

# shell에서 User
# from django.contrib.auth import get_user_model
# User = get_user_model()
# User.objects.all()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6) # validators=[]