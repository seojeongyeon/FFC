from django import forms
from .models import Cafe,Comment


class CafePost(forms.ModelForm):
    # mainimage = forms.ImageField(upload_to='images/', required = False)
    # image1 = forms.ImageField(upload_to='images/', required = False)
    # image2 = forms.ImageField(upload_to='images/', required = False)
    # image3 = forms.ImageField(upload_to='images/', required = False)
    # image4 = forms.ImageField(upload_to='images/', required = False)
    class Meta:
        model = Cafe
        fields = ['name','address','phonenumber','start_time','end_time','holiday','content','menu','socket','mainimage','image1','image2','image3','image4',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','score',)

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'배려와 매너가 밝은 커뮤니티를 만듭니다.','class':'form-control','rows':5}),
        }
