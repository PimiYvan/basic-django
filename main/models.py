from django.db import models

# Create your models here.
class Student(models.Model):
    TYPE = [
        ('scientist', 'SCIENTIST'),
        ('engineer', 'ENGINEER'),
        ('phisic', 'PHYSIC')
    ]
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone =  models.CharField(max_length=255, null=True, blank=True)
    age =  models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True, choices=TYPE, default='engineer')
    city = models.CharField(max_length=255, null=True, blank=True)
    # def __str__(self, instance) -> str:
    #     return instance.name
