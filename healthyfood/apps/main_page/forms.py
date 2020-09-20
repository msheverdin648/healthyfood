from django import forms

from .models import Buy


class OrderForm(forms.ModelForm):

    class Meta:
        model = Buy
        fields = (
            'first_name', 
            'last_name', 
            'phone', 
            'address',
            'buying_type', 
            'comment',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].label = 'Имя*'
        self.fields['last_name'].label = 'Фамилия*'
        self.fields['phone'].label = 'Телефон*'
        self.fields['address'].label = 'Адрес*'
