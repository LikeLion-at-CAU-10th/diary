from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        # user.profile = self.cleaned_data['profile']
        user.save()