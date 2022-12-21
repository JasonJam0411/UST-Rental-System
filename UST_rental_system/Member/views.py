from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import MemberModelForm, LoginModelForm
from .models import Member
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.


def register(request):
    form = MemberModelForm()
    context = {}
    if request.method == "POST":
        form = MemberModelForm(request.POST, request.FILES)
        if form.is_valid():
            # email = form.cleaned_data['email']
            # print(email)
            form.save()
            context['successful_submit']=True
            #return redirect('register')
    
    context['form']=form

    return render(request, 'register.html', context)

#登入
@csrf_exempt
def login(request):
    form = LoginModelForm()
    context = {}
    if request.method == "POST":
        form = LoginModelForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #email與password是否存在Member table中
            if Member.objects.filter(email=email, password=password).exists():

                #GET Member的name和identity
                member_data = Member.objects.filter(email=email, password=password).values("id","name","identity")
                
                id = member_data[0]["id"]
                name = member_data[0]["name"]
                identity = member_data[0]["identity"]
                
                #存入session
                request.session['id'] = id
                request.session['email'] = email
                request.session['name'] = name
                request.session['identity'] = identity
                
                #一般使用者登入跳轉到home_member.html
                if identity == 1:
                    return redirect('/rental/search_site/')
                
                #缺場材管理、系統管理登入URL
                else:
                    context = {
                        'successful_submit':True
                    }
                    messages.success(request, "場材管理、系統管理登入成功")
                    return HttpResponseRedirect(request.path_info)
            else:
                messages.error(request, "email或密碼輸入錯誤")
                return HttpResponseRedirect(request.path_info)
    
    context['form']=form
    return render(request, 'login.html', context)            

#登出
def logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect('/member/login/')
    