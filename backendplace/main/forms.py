from .models import Tablish
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TablishForm(ModelForm):
    class Meta:
        model = Tablish
        fields = ['title', 'memory_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название места"
        }),
            "memory_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ваше воспоминание"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Дата публикации"
            })
        }

