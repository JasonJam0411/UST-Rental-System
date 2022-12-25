from django import forms
from .models import *


class AddEquModelForm(forms.ModelForm):
    
    class Meta:
        model = Equipment
        fields = ('name','usage', 'price','image','number','department_id','rule' ) #

        #choices
        usage_choices = [('運動','運動'),('會議','會議')]

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'usage': forms.Select(choices=(usage_choices), attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'min':'10'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}), 
            'number': forms.NumberInput(attrs={'min':'1'}), 
            'rule': forms.Textarea(attrs={'class': 'form-control'}),
            'department_id': forms.NumberInput(attrs={'min':'1'}),
        }
        
        labels = {
            'name': '名稱',
            'usage': '用途',            
            'price': '價格',
            'image': '圖片',
            'number': '數量',
            'rule':'租借規則',
            'department_id':'單位'
        }

class AddSiteModelForm(forms.ModelForm):
    
    class Meta:
        model = Site
        fields = ('name','usage', 'address', 'location', 'price', 'image', 'rule', 'department_id')
        
        #choices
        usage_choices = [('運動','運動'), ('會議','會議')]

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'usage': forms.Select(choices=(usage_choices), attrs={'class': 'form-select'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'location':forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'min':'1'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'rule': forms.Textarea(attrs={'class': 'form-control'}),
            'department_id': forms.NumberInput(attrs={'min':'1'}),

        }

        labels = {
            'name': '名稱',
            'usage': '用途',
            'address': '地址',
            'location': '地點',
            'price': '價格',
            'image': '租借圖片',
            'rule': '租借規則',
            'department_id': '單位'
        }

class UpdateSiteForm(forms.ModelForm):
    
    class Meta:
        model = Site
        fields = ('name','usage','address','location','price','image','rule')
        
        #choices
        usage_choices = [('運動','運動'), ('會議','會議')]
    

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'usage': forms.Select(choices=(usage_choices), attrs={'class': 'form-select'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'location':forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'min':'10'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'rule':forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        
        labels = {
            'name': '名稱',
            'usage': '用途',
            'address':'地址',
            'location':'地點',
            'price': '價格',
            'image': '圖片',
            'rule': '租借規則',
        }

class UpdateEquForm(forms.ModelForm):
    
    class Meta:
        model = Equipment
        fields = ('name','usage','price','image','number','rule')
        
        #choices
        usage_choices = [('運動','運動'), ('會議','會議')]
    
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'usage': forms.Select(choices=(usage_choices), attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'min': '10'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'min': '1'}),
            'rule':forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'name': '名稱',
            'usage': '用途',
            'price': '價格',
            'image': '圖片',
            'number': '數量',
            'rule': '租借規則',
        }