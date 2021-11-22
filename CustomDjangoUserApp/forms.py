from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(widget = forms.EmailInput(attrs = { 'id' : 'email-input', 'class' : 'form-input', 'placeholder' : 'Email Address'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = { 'id' : 'password-input', 'class' : 'form-input', 'placeholder' : 'Password', 'label' : 'Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = { 'id' : 'confirm-password-input', 'class' : 'form-input', 'placeholder' : 'Confirm Password', 'label' : 'Confirm Password'}))

    class Meta: 
        model = User
        fields = '__all__'

class AdminCreationForm(forms.ModelForm):

    email = forms.EmailField(widget = forms.EmailInput(attrs = { 'id' : 'email-input', 'class' : 'form-input', 'placeholder' : 'Email Address'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = { 'id' : 'password-input', 'class' : 'form-input', 'placeholder' : 'Password', 'label' : 'Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = { 'id' : 'confirm-password-input', 'class' : 'form-input', 'placeholder' : 'Confirm Password', 'label' : 'Confirm Password'}))

    class Meta:
        model = User
        fields = '__all__'

    # checking the validity of the passwords entered into the form
    def clean_password(self): 

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 is not None and password1 != password2:
            raise forms.ValidationError('Passwords Do Not Match')
        return password1

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        return user

class AdminChangeForm(forms.ModelForm):

    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            'email'
        ]

    def clean_password(self):
        return self.initial('password1')