from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDevice(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    device = models.CharField(max_length=20)

class HealthReport(models.Model):

    device = models.ForeignKey(EmployeeDevice,on_delete=models.CASCADE)
    temprature = models.IntegerField(max_length=20)
    glucose = models.IntegerField(max_length=20)
    pulse = models.IntegerField(max_length=20)
    created_time = models.DateTimeField()
