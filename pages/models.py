from django.db import models

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    # first parameter of this foregign key is use to create relationship with other model
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    username = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField(max_length=15)
    text_message = models.TextField(max_length=20, blank=True)
    # giving choices with key and values
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    user_image = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)

    # this auto now add will add new entry and only auto_now will update
    user_date = models.DateField(auto_now_add=True)

    register_date = models.DateTimeField(default=datetime.now) # to fix Note: You are 5.5 hours ahead of server time. |
    # search list of database timezones

    def __str__(self):
        return self.username

    # use to display new contact_id in first position
    class Meta:
        ordering = ['-id']