from django import forms


class MessageForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email or Phone number...",
                "class": "form-input",
                "autocomplete": "username",
            }
        ),
        label="Email or Phone number",
    )
    message = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter the password...",
                "class": "form-input password-input",
                "autocomplete": "current-password",
                "data-password-input": "true",
            }
        ),
        label="Password",
    )
