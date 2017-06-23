from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Datatable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    text = models.CharField(max_length=100)
    number = models.FloatField()
    data = models.FloatField()
    volume = models.IntegerField()
    image = models.ImageField(upload_to="Images/",default='Images/No-img.jpg')

    def __str__(self):
        return self.text
