from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateField(auto_now=True, blank=True)
    def __str__(self):
        return f" message from {self.name} - {self.email}"    
class Author(models.Model):
    Aname = models.CharField(max_length=255)
    Ainstalnk = models.CharField(max_length=13)
    Aemail = models.CharField(max_length=100)
    Aautabout = models.TextField()
    def __str__(self):
        return self.Aname    
