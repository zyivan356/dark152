from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'email_form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_form'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('This user does not exist!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Wrong password!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Account disabled')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label="Enter the email", widget=forms.EmailInput(attrs={'class': 'email_form'}))
    username = forms.CharField(
        label="Enter the username", widget=forms.TextInput(attrs={'class': 'username_form'}))
    password = forms.CharField(
        label="Enter the password", widget=forms.PasswordInput(attrs={'class': 'password_form'}))
    password2 = forms.CharField(
        label="Confirm the password", widget=forms.PasswordInput(attrs={'class': 'password2_form'}))

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('Email is taken!')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords do not match")
        return data["password2"]
