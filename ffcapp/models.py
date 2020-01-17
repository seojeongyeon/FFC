from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Cafe(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=150, null=True)
    phonenumber = models.CharField(max_length=20,null=True)
    start_time = models.TimeField('start_time',null=True)
    end_time = models.TimeField('end_time',null=True)
    holiday = models.CharField(max_length=27,null=True)
    content = models.CharField(max_length=1500, null=True) #태그
    menu = models.ImageField(upload_to='images/',null=True, blank = True)
    choice = (
        ('yes', '있음'),
        ('no', '없음'),
        ('soso', '적당히 있음'),
    )
    socket = models.CharField(max_length=4, choices=choice,null=True)
    mainimage = models.ImageField(upload_to='images/', null=True, blank = True)
    image1 = models.ImageField(upload_to='images/', null=True, blank = True)
    image2 = models.ImageField(upload_to='images/', null=True, blank = True)
    image3 = models.ImageField(upload_to='images/', null=True, blank = True)
    image4 = models.ImageField(upload_to='images/', null=True, blank = True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    writer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Cafe, related_name='comments', on_delete = models.CASCADE)
    text = models.TextField(blank = True)
    created_date = models.DateTimeField(default=timezone.now,blank = True)
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],help_text="방문했던 카페는 어떠셨나요? 점수를 입력해주세요(1~5점)", default=True, blank = True)

    def __str__(self):
        return self.text
