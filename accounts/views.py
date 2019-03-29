from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from accounts.forms import UserForm, ProfileForm
from accounts.models import Profile


def home(request):
    pass

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm
    context = {'form':form}
    return render(request,'signup.html',context)

def profile(request,slug):
    p = get_object_or_404(Profile,slug=slug)
    u = request.user
    if str(u) == str(slug):
        edit = True
    else:
        edit = False
    context = {'p':p,'u':u,'edit':edit,'slug':slug}
    return render(request,'profile.html',context)

def edit_profile(request):
    p = request.user
    profile = get_object_or_404(Profile,slug=p)
    if request.method == 'POST':
        user_form = UserForm(request.POST,request.FILES,instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    print(p)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    }
    return render(request,'edit_profile.html',context)