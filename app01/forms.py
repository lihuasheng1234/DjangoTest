from django import forms
from . import models


class TestForm(forms.Form):
    name = forms.CharField(max_length=10,min_length=5,label='姓名')


class TestFormUses(forms.Form):
    name = forms.CharField(max_length=10,min_length=5,label='姓名')

class TestModelFormUses(forms.ModelForm):
    age = forms.IntegerField(label='年龄')
    class Meta:
        model = models.Userinfo
        fields = ['name']
    def clean_name(self):
        if self.cleaned_data['name'] == 'root':
            print("敏感")
        return self.cleaned_data['name']

class TestFileFieldForm(forms.Form):
    name = forms.CharField(label="姓名",max_length=10)
    selfpic = forms.FileField(label="头像")
