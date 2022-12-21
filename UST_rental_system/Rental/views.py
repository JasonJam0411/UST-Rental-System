from django.shortcuts import render, redirect
from Rental.models import Duration, Site, Rent_Site
from Member.models import Member
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime

#回首頁
def back_to_index(request):
    if request.method == "POST":
        return redirect('/rental/search_site/')



#搜尋場地
def search_site(request):
    if 'email' not in request.session:
        return redirect('/member/login/')
    else:
        if 'rent_site_turn_page' in request.session:
            del request.session['rent_site_turn_page']
        
        context = {}

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
 
#顯示欲預約場地
def display_reserve_site(request):
    if 'email' not in request.session:
        return redirect('/member/login/')
    else:
        context={}
        if request.method == "POST":
            id = request.POST['reserve_site_duration_id']
            result = Duration.objects.filter(id = id)
            context["reserve_site_duration"] = result
            turn_page = request.session.get('rent_site_turn_page')
            if( turn_page == 1):
                context["successful_submit"] = True
            return render(request, "rent_site.html", context)


#確定預約場地
def reserve_site(request):

    if request.method == "POST":

        #檢查是否場地已被預約
        id = request.POST['reserve_site_duration_id']
        result = Duration.objects.filter(id = id).values('rent_status')
        rent_status = result[0]['rent_status']

        if rent_status == 1:
            messages.error(request, "你慢了一步! 該場地已被其他使用者預約!")
            request.session['rent_site_turn_page'] = 0
            return display_reserve_site(request)
        else:
            request.session['rent_site_turn_page'] = 1
            #確定預約場地
            date = datetime.date.today()  # Returns YYYY-MM-DD
            status = 0 #未付款狀態
            timestamp = datetime.datetime.now() # Returns YYYY-MM-DD HH:MM
            member_id = request.session.get('id')
            
            Rent_Site.objects.create(  #Rent_site資料庫新增一筆資料
                date=date,
                status=status,
                timestamp=timestamp,
                member_id=Member.objects.get(id = member_id),
                duration_id=Duration.objects.get(id = id),
            )
            
            #duration table 改租借狀態
            Duration.objects.filter(id=id).update(rent_status=1)

            messages.success(request, "預約場地成功! 請盡速至繳費地點繳費，否則將取消場地預約")
            return display_reserve_site(request)

