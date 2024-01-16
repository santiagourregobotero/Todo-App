from typing import Any
from django import forms
from todoapp.models import User,Tasks
from django.db.models import Q
    



class RegisterUser(forms.Form):

    username = forms.CharField(min_length=5)
    password1 = forms.CharField(min_length=5)
    password2 = forms.CharField(min_length=5)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError("User with such username already exits")
        
        return username
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("Both password doesnt exits")
        return self.cleaned_data
    
    def save(self):
        user = User(username=self.cleaned_data.get("username"))
        user.set_password(self.cleaned_data.get("password1"))
        user.save()
        return user
        

class LoginUser(forms.Form):
    username= forms.CharField()
    password = forms.CharField()

    # def clean(self):
    #     user = User.objects.filter(Q(username=self.cleaned_data.get("username")) & (Q(password=self.cleaned_data.get("passsword"))))
    #     if not user:
    #         raise forms.ValidationError("User with such credential doesnt exits")
    #     return self.cleaned_data



class TasksForm(forms.ModelForm):
    due_date = forms.DateField()
    class Meta:
        model = Tasks
        fields= ["id","title","description","is_completed","priority","due_date"]
