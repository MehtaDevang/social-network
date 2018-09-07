from django.shortcuts import render
from django.http import HttpResponse
# 500607847081584
# d469df5684ce705dcf8808b617a5ee4d
# Create your views here.
from django.contrib.auth.models import User
from . models import OurUsers
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def adduser(request):
    name = request.POST['name']
    dob = request.POST['dob']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if not OurUsers.objects.filter(username = username).exists():
        db = OurUsers()
        db.name = name
        db.username = username
        db.dob = dob
        if(password1 == password2):
            db.password = password1
        else:
            return HttpResponse("Passwords do not match")
        db.save()
        return HttpResponse("user added to the database")

    else:
        return HttpResponse("user already exists")

def check_login(request):
    user = request.POST['username']
    password = request.POST['password']
    print(user)
    print(OurUsers.objects.get(username = user))

    if OurUsers.objects.get(username = user):
        the_user = OurUsers.objects.get(username = user)
        print(the_user.password == password)
        if(the_user.password == password):
            return render(request, 'home.html')
        else:
            return HttpResponse("incorrect password")
    else:
        return HttpResponse("user does not exist")

def home(request):
    return render(request, 'home.html')