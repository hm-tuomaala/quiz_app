from django.shortcuts import render, redirect
from clogin.forms import LoginForm
from .models import Keys


def login(request):

    youcanpass = False
    login_form = LoginForm()
    context = {
        'name' : '',
        'form' : login_form
    }
    passkey = ''

    if request.method == 'POST':
        # Form was submitted lets parse the data
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            for key in Keys.objects.all():
                if key.key == login_form.cleaned_data['key'] and not key.used:
                    youcanpass = True
                    passkey = key.key
                    key.name = login_form.cleaned_data['name']
                    context['name'] = key.name
                    key.used = True
                    key.save()
        else:
            context = {'reason':'name'}

        if youcanpass:
            # Render quiz if lofin was successful
            return redirect('quiz-home', passkey)
        else:
            # Render something else if access was denied
            return render(request, 'clogin/denied.html', context)
    else:
        # Render login when page is reloaded or entered for the first time
        return render(request, 'clogin/login.html', context)
