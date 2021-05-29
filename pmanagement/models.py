from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
# Table
class Users(models.Model):
# props - columns
    UniqueID = models.CharField(max_length=10)
    UserName = models.CharField(max_length=10)
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    DOB = models.DateField(blank=True,null=True)
    Password = models.CharField(max_length=34)

    def dateofbirth(self):
        self.DOB = timezone.now()
        self.save()

    def __str__(self):
        return self.FullName