from django.shortcuts import render
from .models import AccountUser
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html',
      {'users': users})    

def signup(request):
    # breakpoint()
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'],
                                            password=request.POST['password1'])
            user.save()
            # login(request, user)
        #retirm login page
        return render(request, 'signup.html', {"form":UserCreationForm})  
# Compare this snippet from greysend_project/accounts/models.py:


def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    elif request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #to implement "profile.html"
            return redirect('list_users')  
        else:
            #todo: implement error page
            return redirect("error_no_user.html")
        
def log_out(request):
    #get current user
    logout(request)
    return redirect('index')