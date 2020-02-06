from django.db import models
from django.contrib.auth.models import User, Group, Permission

dc_id = models.CharField(max_length=255)
dc_id.contribute_to_class(User, 'dc_id')

class User(User):
    class Meta:
        proxy = True
