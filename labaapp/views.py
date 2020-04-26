
from django.shortcuts import render
from labaapp.models import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from labaapp.forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login


def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('login/')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                 username=cd['username'],
                 password=cd['password'])
        if user is not None:
            if user.is_active:
                 login(request, user)
                 return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'labaapp/login.html', {'form': form})
 
   
def register(request):
    if request.method == 'POST':
         user_form = UserRegistrationForm(request.POST)
         if user_form.is_valid():
             # Создаем нового пользователя, но пока не сохраняем в базу данных.
             new_user = user_form.save(commit=False)
             # Задаем пользователю зашифрованный пароль.
             new_user.set_password(user_form.cleaned_data['password'])
             # Сохраняем пользователя в базе данных.
             new_user.save()
             return render(request,
                     'register_done.html',
                     {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'register.html',{'user_form': user_form})
 

@login_required(login_url='/login')
def userProfile(request):
    all_users = User.objects.values('username').exclude(username=request.user.username)
    content = {'users':all_users,'username':request.user.username}
    return render(request, 'userlist.html', content)

def post(request):
    msgs = Message.objects.all()
    content = {'msgs':msgs,'username':request.user.username}
    return render(request, 'write_message.html', content)
    
def sendMessage(request):
    msg = Message(
        sender=request.user,
        content=request.POST['content']
    )
    msg.save()
    return post(request)