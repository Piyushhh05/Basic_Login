from django.db import models

# Create your models here.
class Details(models.Model):
    nm = models.CharField(max_length=100)
    eml=models.EmailField(max_length=50)
    pno=models.CharField(max_length=50)
    un=models.CharField(max_length=50)
    pw=models.CharField(max_length=20)

    def  __str__(self):
        return self.name