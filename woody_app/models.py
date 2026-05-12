from django.db import models

# Create your models here.

class Orders(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    mobile=models.BigIntegerField(null=False)
    service=models.CharField(max_length=20,null=False)
    budget=models.CharField(max_length=10,null=False)
    note=models.TextField(null=True)