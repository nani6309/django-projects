from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}{self.name}{self.date}{self.time}'

class members(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=254)
    gender=models.CharField(max_length=50)
    dob=models.DateField()
    uid=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.uid} {self.name} {self.mobile} {self.email}{self.gender}{self.dob}'
