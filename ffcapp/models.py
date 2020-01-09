from django.db import models

# Create your models here.

class Cafe(models.Model): 
    name = models.CharField(max_length=20)
    address = models.TextField()
    phonenumber = models.CharField(max_length=20)
    start_time = models.TimeField('start_time')
    end_time = models.TimeField('end_time')
    holiday = models.CharField(max_length=27)
    content = models.TextField() #태그
    cafeimage = models.ImageField(upload_to='images/', default='')
    menu= models.ImageField(upload_to='images/', default='')
    choice = (
        ('yes', '있음'),
        ('no', '없음'),
        ('soso', '적당히 있음'),
    )
    socket = models.CharField(max_length=4, choices=choice)


    def __str__(self):
        return self.name