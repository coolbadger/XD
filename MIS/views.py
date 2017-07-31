from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.

def default(request):
    # request.session['is_login'] = False
    return render(request, 'mis_base/index_base.html')


def master_page(request):
    return render(request, 'mis_page/master_page.html')


def mis_login(request):
    username = ''
    if request.POST:
        username = request.POST['form-username']
        password = request.POST['form-password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['is_login'] = True
            return HttpResponseRedirect('/mis/')
        else:
            request.session['is_login'] = False
    return render(request, 'mis_page/login.html', {'username': username})


def mis_logout(request):
    logout(request)
    request.session['is_login'] = False
    return HttpResponseRedirect('/mis/')
