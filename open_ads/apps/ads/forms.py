from django import forms
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget
from apps.ads.models import Card, CardPhoto
from apps.ads.validators import max_file_size


class CardProductForm(forms.ModelForm):
    photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}),
                              validators=[max_file_size])
    description = forms.CharField(widget=CKEditorWidget(), label='Описание')

    class Meta:
        model = Card
        fields = ('title', 'price', 'id_category', 'condition', 'description', 'photos')


class CardProductUpdateForm(forms.ModelForm):
    photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}),
                              validators=[max_file_size])
    description = forms.CharField(widget=CKEditorWidget(), label='Описание')

    class Meta:
        model = Card
        fields = ('title', 'price', 'condition', 'description', 'photos')

