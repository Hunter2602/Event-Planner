from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    dob = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    event_name = models.CharField(max_length=100, null=True, blank=True)
    def _str_(self):
        return self.user.username

class upcoming_event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True) 

    
    def __str__(self):
        return self.event_name
class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.ForeignKey(upcoming_event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)


