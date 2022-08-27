from django import forms
from django.forms import ModelForm
from .models import Form as model_form


class Form4(ModelForm):
    class Meta:
        model = model_form
        fields = ['delivery_condition', 'country', 'city', 'location', 'zipcode', 'delivery_date', 'delivery_cost', 'type_transport']

        labels = {
            'delivery_condition':'Çatdırılma şərti',
            'country':'Ölkə',
            'city':'Şəhər',
            'location':'Ünvan',
            'zipcode':'Zip kod',
            'delivery_date':'Çatdırılma tarixi',
            'delivery_cost':'Çatdırılma xərci',
            'type_transport':'Nəqliyyat növü'
        }

        widgets = {
            'delivery_condition':forms.Select(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'delivery_date':forms.DateTimeInput(attrs={'class':'form-control'}),
            'delivery_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'type_transport':forms.Select(attrs={'class':'form-control'}),

        }



class Form1(forms.ModelForm):
    class Meta:
        model = model_form
        fields = ["request_number", "user_id", "datetime", "valyuta"]
        
        labels = {
            'request_number': 'Sorğu nömrəsi',
            'user_id':"Müştəri İD",
            'datetime':"Təklifin qüvvədə olduğu müddət",
            'valyuta':'Valyuta'
        }
        
        
        widgets = {
            'request_number': forms.TextInput(attrs={'class':'form-control'}),
            'user_id':forms.TextInput(attrs={'class':'form-control'}),
            'datetime':forms.DateTimeInput(attrs={'class':'form-control'}),
            'valyuta':forms.Select(attrs={'class':'form-control'}),
        }


class Form2(forms.ModelForm):
    class Meta:
        model= model_form
        fields = ["miqdar", "price", "edv_price","edv_degree","product"]
        
        labels = {
            'miqdar':'Miqdar',
            'price':'Vahidin qiyməti',
            'edv_degree':'ƏDV drərəcəsi',
            'edv_price':'ƏDV məbləği',
            }

        widgets = {
            'miqdar':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'edv_degree':forms.NumberInput(attrs={'class':'form-control'}),
            'edv_price':forms.NumberInput(attrs={'class':'form-control'}),
        }
        


class Form3(forms.ModelForm):
    class Meta:
        model= model_form
        fields = ["payment_terms", "bank_account", "discount"]
        
        labels = {
            'payment_terms':'Ödəniş şərti',
            'bank_account':'Bank hesabı',
            'discount':'Endirim',
        }

        widgets = {
            'payment_terms':forms.Select(attrs={'class':'form-control'}),
            'bank_account':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.Select(attrs={'class':'form-control'}),
        }

