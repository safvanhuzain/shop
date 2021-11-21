from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default='false')