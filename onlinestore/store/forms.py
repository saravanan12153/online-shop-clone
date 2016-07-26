from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    """Define registration from based on User model,
    with validation on username and password fields."""

    # class Meta:
    # model = User
    # fields = ('username', 'password',)

    username = forms.RegexField(regex=r'^[0-9a-zA-Z_]*$',
                                max_length=30,
                                widget=forms.TextInput(attrs=dict(
                                    required=True,
                                    render_value=False)),
                                label='Username')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True,
                   render_value=False)),
        label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True,
                   render_value=False)),
        label='')

    def clean_username(self):
        """Check that the passed in username does not exist."""
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except ObjectDoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username has been used")

    def clean(self):
        """Check that the passed in password and confirmation match."""
        try:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("Passwords do not match")
        except KeyError:
            return self.cleaned_data

    def save(self):
        """Save the newly created user."""
        new_user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        return new_user


class LoginForm(forms.Form):
    """Define form for user login."""

    username = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, autocomplete='off')))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True)))
