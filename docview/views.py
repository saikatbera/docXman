from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'docview/index.html')
    #return HttpResponse("Hello")
def signUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'docview/signup.html', {'form': form})
    #return render(request, 'docview/signup.html')
def mainView(request):    
    return render(request, 'docview/main.html')

#from django.shortcuts import render, redirect

    
