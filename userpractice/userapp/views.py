from django.shortcuts import render
from userapp.forms import UserForm, UserProfileDataForm

#Special libraries for Password authentication
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'userapp/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_data_form = UserProfileDataForm(data=request.POST)

        if user_form.is_valid and user_profile_data_form.is_valid:
            user = user_form.save()
            user.set_password(user.password) #Hash the password
            user.save()

            user_profile = user_profile_data_form.save(commit=False)
            user_profile.user = user # Set the foriegn key
            # Set the profile picture to the UserProfileData profile_pic field
            if 'profile_imgs' in request.FILES:
                user_profile.user_profile_pic = request.FILES['profile_imgs']
            user_profile.save()

            registered = True
        else:
            print(user_form.errors, user_profile_data_form.errors)
    else:
        user_form = UserForm()
        user_profile_data_form = UserProfileDataForm()
    return render(request,'userapp/register.html',{'user_form': user_form,
                                                    'user_profile_data_form': user_profile_data_form,
                                                    'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        #Check if the user is autheticated
        if user:
            #Check if the user is active
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('userapp:index')) #reverse is like a URL template
            else:
                return HttpResponse("USER IS INACTIVE!")
        else:
            print("Someone has tried to login with your access data. Keep an Eye!")
            print("username: {}, password: {}".format(username,password))
            HttpResponse("Invalid Username and Password")
    else:
        return render(request,'userapp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userapp:afterlogout'))

def after_logout(request):
    return render(request,'userapp/afterlogout.html')
