from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from show.models import UserDetails


# Create your views here.

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        obj = User.objects.create_user(username=username,
                                       first_name=firstname, last_name=lastname
                                       , email=email, password=password)
        obj.save()
    return render(request, "registration.html")


def user_login(request):
    data = request.POST
    if request.method == "POST":
        username = data['username']
        password = data['password']
        obj = authenticate(username=username, password=password)
        if obj is not None:
            login(request, obj)
            return redirect('profile')
    return render(request, 'login_temp.html')


@login_required()
def user_profile(request):
    if request.method == 'POST':
        data = request.POST
        fname = data['firstname']
        lname = data['lastname']
        mobile = data['mobile']
        gender = data['gender']
        age = data['age']
        user_obj = User.objects.get(username=request.user.username)
        if UserDetails.objects.filter(user_data_id=user_obj.id).exists():
            obj = UserDetails.objects.get(user_data_id=user_obj.id)
            obj.first_name = fname
            obj.last_name = lname
            obj.mobile = mobile
            obj.gender = gender
            obj.age = age
            obj.save()
            return redirect('profile')
        obj = UserDetails.objects.create(user_data_id=user_obj.id, first_name=fname,
                                         last_name=lname,
                                         mobile=mobile, gender=gender, age=age)
        obj.save()
        return redirect("profile")
    # data = UserDetails.objects.get(user_data_id=User.objects.get(username=request.user.username))
    return render(request, 'profile.html')

@login_required()
def user_delete(request, id):
    data = UserDetails.objects.get(user_data_id=id)
    data.delete()
    return render(request, 'registration.html')
