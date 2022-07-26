from django import forms

pw_options = [('upper', 'Uppercase'), ('lower', 'Lowercase'), ('numb', 'Numbers'), ('spec', 'Special Characters')]

class PasswordForm(forms.Form):
    length = forms.IntegerField(label='Password Length (between 8 & 128 characters', min_value=8, max_value=128, required = True)
    pw_choices = forms.MultipleChoiceField(
        label='Choose at least one...',
        required= True,
        widget=forms.CheckboxSelectMultiple,
        choices=pw_options,
    )
    
    