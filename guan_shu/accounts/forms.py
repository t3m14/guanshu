from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Удаляем help_text для всех полей формы
        for field in self.fields.values():
            field.help_text = None
        
        # Remove password confirmation field
        if 'password2' in self.fields:
            del self.fields['password2']
            
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1')