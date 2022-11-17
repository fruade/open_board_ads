from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=16, min_length=2, error_messages={
        'max_length': 'Слишком много символов',
        'min_lenght': 'Слишком мало символов',
        'required': 'Укажите хотя бы 2 символа'
    })
    email = forms.EmailField(label='Email')
    rating = forms.IntegerField(label='Оцените сайт от 1 до 5', max_value=5, min_value=1)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 30}), label='Отзыв')
