from django import forms

class UserSearch(forms.Form):
    search = forms.CharField(label='Поиск друзей',
                               widget=forms.TextInput)
    def __init__(self, *args, **kwargs):
        super(UserSearch, self).__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите запрос'})