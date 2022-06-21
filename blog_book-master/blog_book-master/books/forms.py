from email.policy import default
from django import forms

class Books_form(forms.Form):
    isbn = forms.IntegerField()
    title = forms.CharField(max_length = 100)
    publication_date = forms.DateField()
    price = forms.FloatField()
    synopsis = forms.CharField(max_length=300, required = False)
    edition = forms.IntegerField(required = False)
    # cover = forms.ImageField(required = False)
    active = forms.BooleanField(required = False, initial = True)

class Authors_form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length = 50)
    middle_name = forms.CharField(max_length = 10, required=False)
    surname = forms.CharField(max_length = 100)
    nickname = forms.CharField(max_length = 25, required=False)
    birthday = forms.DateField()
    active = forms.BooleanField(required = False, initial = True)

class Editorials_form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length = 50)
    founder = forms.CharField(max_length = 50, required=False)
    foundation_date = forms.DateField(required=False)
    country = forms.CharField(max_length = 50, required=False)
    main_organization = forms.CharField(max_length = 50, required=False)
    # logo = forms.ImageField(required = False)
    active = forms.BooleanField(required = False, initial = True)
    
class Genres_Form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length = 50)
    description = forms.CharField(max_length = 100, required = False)
    active = forms.BooleanField(required = False, initial = True)
