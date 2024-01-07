from django.db import models

# Create your models here.
class slotbooking(models.Model):
    CHECK_IN_DATE = models.DateField(null=True)
    CHECK_OUT_DATE = models.DateField(null=True)
    NUMBER_OF_PERSON = models.IntegerField(null=True)
    STATUS = models.CharField(max_length=20,null=True)

class guestmessage(models.Model):
    Name = models.CharField(max_length=20,null=True)
    Email = models.EmailField(null=True)
    Message = models.CharField(max_length=100,null=True)