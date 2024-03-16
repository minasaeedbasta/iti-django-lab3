from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from users.forms import  UserModelForm
# Create your views here.

def profile(request):
    url = reverse('books.index')
    return redirect(url)


def create_user(request):
    form = UserModelForm()
    if request.method=='POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("user created successfully")
    return render(request,'users/create_user.html', {'form': form})