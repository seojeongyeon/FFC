from django.db import models

# Create your models here.

class Cafe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    phonenumber = models.CharField(max_length=20,null=True)
    start_time = models.TimeField('start_time',null=True)
    end_time = models.TimeField('end_time',null=True)
    holiday = models.CharField(max_length=27,null=True)
    content = models.TextField(null=True) #태그
    menu = models.ImageField(upload_to='images/',null=True)
    choice = (
        ('yes', '있음'),
        ('no', '없음'),
        ('soso', '적당히 있음'),
    )
    socket = models.CharField(max_length=4, choices=choice,null=True)


    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', default='', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', default='', blank=True, null=True)