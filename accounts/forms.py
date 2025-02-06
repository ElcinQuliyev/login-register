from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password'
        }
    ))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'image',
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }),
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        print(confirm_password)
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return super().clean()

    def save(self, commit: bool = ...):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(max_length=200, widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
        })
    )

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields = [
                'username',
                'last_name',
                'bio',
                'email',
                'password',
                'image',
            ]