from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import Book



class BookForm(forms.ModelForm):
    name = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'Your Full Name'}))   
    email= forms.EmailField(required= True, widget= forms.TextInput
                           (attrs={'placeholder':'your_mail@example.com'}))  
    subject = forms.CharField(required= True, widget= forms.TextInput
                           (attrs={'placeholder':'Vacancy / Field in which you are Applying'}))  
                                 
    skill_1 = forms.CharField(required=False,   widget= forms.TextInput
                           (attrs={'placeholder':'Additional information'}))
    skill_2 = forms.CharField(required=False,  widget= forms.TextInput
                           (attrs={'placeholder':'Additional information'}))
    skill_3 = forms.CharField(required=False,  widget= forms.TextInput
                           (attrs={'placeholder':'Additional information'}))
    skill_4 = forms.CharField(required=False,  widget= forms.TextInput
                           (attrs={'placeholder':'Additional information'}))
    skill_5 = forms.CharField(required=False,  widget= forms.TextInput
                           (attrs={'placeholder':'Additional information'}))
    phone_no = PhoneNumberField()                 
    class Meta:
        model = Book
        fields = ('name', 'email','subject','skillset','skill_1','skill_2','skill_3','skill_4','skill_5','phone_no','pdf', 'cover')
