from django import forms
from .models import Cafe,Image


class CafePost(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name','address','phonenumber','start_time','end_time','holiday','content','menu','socket']

class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image1','image2','image3',]
