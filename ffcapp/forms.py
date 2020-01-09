from django import forms
from .models import Cafe


class CafePost(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name','address','phonenumber','start_time','end_time','holiday','content','cafeimage','menu','socket']