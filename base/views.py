from django.shortcuts import render
from base.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from base.models import UserProfileInfo

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                p=UserProfileInfo.objects.get(user_id=user)
                if p.registered_as=="Patient":
                    return HttpResponseRedirect(reverse('base:search'))
                elif p.registered_as=="Donor":
                    return HttpResponseRedirect(reverse('base:request'))

                # return HttpResponse("login sucessful")


            else:
                return HttpResponse("account not active")
        else:
            print("fail")
            return HttpResponse("Invalid login")
    else:
        return render(request,'base/user_login.html',{})

def search(request):
    searched=True
    if request.method == 'POST':
        searched=False
        bT = request.POST.get('blood_type')
        object = UserProfileInfo.objects.all().filter(blood_type=bT)

        return render(request,'base/search.html',context={"matches":object})
    else:
        return render(request,'base/search.html',context={"searched":searched})



def requests(request):
    return render(request,'base/requests.html',context={"print":"requests page"})
