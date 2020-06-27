from django.shortcuts import render
from base.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'base/home.html',context={"print":"hompage"})
# Create your views here.
def contact(request):
    return render(request,'base/contact_us.html',context={"print":"contact us page"})

def register(request):
    registered=False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'base/register.html',
                              {'user_form':user_form,
                              'profile_form':profile_form,
                              'registered':registered})

def user_login(request):
    return render(request,'base/user_login.html',context={"print":"login page"})

def search(request):
    return render(request,'base/user_login.html',context={"print":"search page"})
