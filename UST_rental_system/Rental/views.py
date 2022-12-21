from django.shortcuts import render, redirect
from Rental.models import Duration

#一般使用者-搜尋場地
def member_search_site(request):
    if 'email' not in request.session:
        return redirect('/member/login/')
    else:
        context = {}
        print(request.session.get("email"))

        if request.method == "POST":
            school = request.POST['school']
            usage = request.POST['usage']
            date = request.POST['date']
            start = int(request.POST['start'])
            end = int(request.POST['end'])

            end_first = start+1
            start_last =end-1

            result = Duration.objects.filter(
            site_id__department_id__school_id = school,
                    site_id__usage = usage,
                    date = date,
                    rent_status = 0,
                    start__gte = start,
                    start__lte = start_last,
                    end__gte = end_first,
                    end__lte = end
                )

            context["condition_query_set"] = result
            return render(request, "index.html", context)

        return render(request, "index.html", context)
 
 #預約場地
def member_display_reserve_site(request):
    
    return render(request, "index.html")




# def login(request):
#     form = LoginModelForm()
#     context = {}
#     if request.method == "POST":
#         form = LoginModelForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             #email與password是否存在Member table中
#             if Member.objects.filter(email=email, password=password).exists():

#                 #GET Member的name和identity
#                 member_data = Member.objects.filter(email=email, password=password).values("name","identity")
#                 context = {
#                     'status':'True',
#                     'member_data':member_data,
#                     'successful_submit':True
#                 }
#                 messages.success(request, "登入成功")
#                 #要改成跳頁
#                 return HttpResponseRedirect(request.path_info)

#             else:
#                 messages.error(request, "email或密碼輸入錯誤")
#                 return HttpResponseRedirect(request.path_info)
    
#     context['form']=form
#     return render(request, 'login.html', context)            
