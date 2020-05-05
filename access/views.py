from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
# Create your views here.

def Register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/sign_up.html', {'form': form})