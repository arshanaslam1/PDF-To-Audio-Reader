from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms.widgets import NumberInput
from .models import User
from .validators import age_validator
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class AccountRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), validators=[age_validator])
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}), )
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2']


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'autofocus': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'text-left inline_label', 'placeholder': 'Password', 'required': False}))


class AccountPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'type': 'email',
        'name': 'email'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email


class AccountPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetConfirmForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label="New password",
                                    widget=forms.PasswordInput(attrs={
                                        'placeholder': 'New password',
                                    }))
    new_password2 = forms.CharField(label="New password confirmation",
                                    widget=forms.PasswordInput(attrs={
                                        'placeholder': 'New password confirmation',
                                    }))


class AccountUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(validators=[age_validator],
                                    widget=NumberInput(
                                        attrs={'type': 'date',
                                               }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'date_of_birth', 'avatar']


class AccountChangeEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']