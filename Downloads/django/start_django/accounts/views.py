# Create your views here.
# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            id=request.POST['id'],
                                            PW=request.POST['PW'],
                                            firstName=request.POST['firstName'],
                                            lastName=request.POST['lastName'],
                                            SSN=request.POST['ssn'],
                                            age=request.POST['age'],
                                            sex=request.POST['sex'],
                                            phone=request.POST['phone']
                                            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')