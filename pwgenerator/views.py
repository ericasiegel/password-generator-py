from ast import Pass
from django.shortcuts import render
from .forms import PasswordForm
from .password import get_password

def home(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = PasswordForm()
            password = get_password(length = data['length'], choices = data['pw_choices'])
    else:
        form = PasswordForm()
        password = ''
        
    return render(request, 'home.html', { 'form' : form, 'password' : password })