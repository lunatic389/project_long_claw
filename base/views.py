from django.shortcuts import render

def index(request):
    return render(request,'base/home.html',context={"print":"hompage"})
# Create your views here.
def contact(request):
    return render(request,'base/contact_us.html',context={"print":"contact us page"})

def register(request):
    return render(request,'base/register.html',context={"print":"register page"})

def user_login(request):
    return render(request,'base/user_login.html',context={"print":"login page"})

def search(request):
    return render(request,'base/user_login.html',context={"print":"search page"})
