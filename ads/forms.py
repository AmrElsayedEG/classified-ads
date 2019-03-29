from django import forms

from ads.models import Products, Comments, Favorites


class newform(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('title','price','about','categories','phone','img','country','address')

class commentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
class favoritesForm(forms.ModelForm):
    class Meta:
        model = Favorites
        fields = ()