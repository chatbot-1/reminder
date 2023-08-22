from django.db import models

# Create your models here.

class Setreminder(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    sms = models.IntegerField()


    def __str__(self):
        return self.subject
    
    def __str__(self):
        return f"{self.date} - {self.date.strftime('%d %m, %Y')}"