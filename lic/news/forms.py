from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите заголовок'
        })
        self.fields['body'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Напишите текст'
        })
        self.fields['title'].label = 'Заголовок'
        self.fields['body'].label = 'Новость'