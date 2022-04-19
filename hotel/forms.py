from django import forms
from .models import Room, Guest



class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
    # field = ['title', 'content']
    # title = forms.CharField(label='Title', max_length=255)
    # content = forms.CharField(label='Content', widget=forms.Textarea())

# class GuestForm(forms.ModelForm):
#     class Meta:
#         model = Guest
#         fields = '__all__'

class GuestForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')