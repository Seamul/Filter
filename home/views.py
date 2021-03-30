from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
from .models import Student
from datetime import datetime, timedelta,date
from django.db.models import Q
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

class FilterView(View):
    def get(self, request):
        # <view logic>
        student_detail=Student.objects.all()
        tdhaka=Student.objects.filter(city__icontains='dhaka').count()
        tdinajpur=Student.objects.filter(city__icontains='dinajpur').count()
        trajshahi=Student.objects.filter(city__icontains='rajshahi').count()
        print(tdhaka)
        return render(request,'filter.html',{'student_detail':student_detail,'tdhaka':tdhaka,'tdinajpur':tdinajpur,'trajshahi':trajshahi})
    def post(self, request):
        # <view logic>
        print("-----------------------")
        print(request.POST)
        print(request.POST['dhaka'])
        dhaka=request.POST['dhaka']
        if dhaka!='dhaka':
            dhaka='none'
        print('dhaka',dhaka)
        dinajpur=request.POST['dinajpur']
        
        if dinajpur!='dinajpur':
            dinajpur='none'
        print('dinajpur=',dinajpur)
        rajshahi=request.POST['rajshahi']
        if rajshahi!='rajshahi':
            rajshahi='none'
        print('rajshahi',rajshahi)


        # //////////////////////////////////////////////////////////////////
        sujon=request.POST['sujon']
        if sujon!='sujon':
            sujon='none'
        print('sujon',sujon)
        kamal=request.POST['kamal']
        if kamal!='kamal':
            kamal='none'
        print('kamal',kamal)
        monir=request.POST['monir']
        if monir!='monir':
            monir='none'
        print('monir',monir,)

        # /////////////////////////////////////////////////////
        yesterday=request.POST['yesterday']
        print('ppp=',yesterday)
        if yesterday =='1':
            yesterday = date.today() - timedelta(days=1)
        else:
            yesterday=date.today().replace(day=1) + timedelta(days=900000)
        print('yesterday',yesterday)
        
        lastweek=request.POST['lastweek']
        if lastweek=='1':
            lastweek = date.today() - timedelta(days=7)
        else:
            lastweek=date.today().replace(day=1) + timedelta(days=900000)
        print('lastweek',lastweek)
        lastmonth=request.POST['lastmonth']
        if lastmonth=='1':
            last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
            lastmonth = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
        else:
            lastmonth=date.today().replace(day=1) + timedelta(days=90000)
        print('lastmonth',lastmonth)


        # /////////////////////////////////////////////////////////////
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        if not startdate and not enddate:
            startdate=date.today().replace(day=1) + timedelta(days=90000)
            enddate=date.today().replace(day=1) - timedelta(days=90000)
        if startdate and not enddate:
            enddate=date.today().replace(day=1) + timedelta(days=90000)
        if not startdate and  enddate:
            startdate=date.today().replace(day=1) - timedelta(days=90000)
        print('startdate',startdate)
        print('enddate',enddate)


        # ////////////////////////////////////////////////////////////////////////
        passed=request.POST['pass']
        print('passed',passed)
        fail=request.POST['fail']
        print('fail',fail)
        passed_range=0
        fail_range=101
        if passed=='1' and fail =='1':
            passed_range=0
            fail_range=101
        elif passed=='1' and fail =='0':
            passed_range=33
            fail_range=101
        elif passed=='0' and fail =='1':
            passed_range=0
            fail_range=33
        elif passed=='0' and fail =='0':
            passed_range=101
            fail_range=0
        print('pass_range',passed_range)
        # startdate = startdate.strftime('%y-%m-%d')
        # enddate=enddate.strftime('%y-%m-%d')
        print("fail_range",fail_range)
        #Q(created__gte=startdate,created__lte=enddate)
        #  Q(name__icontains=sujon)|Q(name__icontains=kamal) |Q(name__icontains=monir)| Q(city__icontains=dhaka)| Q(city__icontains=dinajpur) | Q(city__icontains=rajshahi)|Q(created__lte=yesterday)|Q(created__lte=lastweek)|Q(created__lte=lastmonth)|Q(Q(created__gte=startdate)&Q(created__lte=enddate))
        #|Q(created__lte=yesterday)|Q(created__lte=lastweek)|Q(created__lte=lastmonth)|Q(Q(created__gte=startdate)&Q(created__lte=enddate))|Q(Q(marks__gte=passed_range)&Q(marks__lt=fail_range))

        #Q(name__icontains=sujon)|Q(name__icontains=kamal) |Q(name__icontains=monir)| Q(city__icontains=dhaka)| Q(city__icontains=dinajpur) | Q(city__icontains=rajshahi)|Q(created__gte=yesterday)|Q(created__gte=lastweek)|Q(created__gte=lastmonth)|Q(Q(created__gte=startdate)&Q(created__lte=enddate))
        stuobj=Student.objects.filter(Q(name__icontains=sujon)|Q(name__icontains=kamal) |Q(name__icontains=monir)| Q(city__icontains=dhaka)| Q(city__icontains=dinajpur) | Q(city__icontains=rajshahi)|Q(created__gte=yesterday)|Q(created__gte=lastweek)|Q(created__gte=lastmonth)|Q(Q(created__gte=startdate)&Q(created__lte=enddate))|Q(Q(marks__gte=passed_range)&Q(marks__lt=fail_range))).values()
        # stu=Student.objects.all()
        print('stu=',stuobj)
        # stu=dict(stu)
        # print(stu)
        return JsonResponse(list(stuobj), safe=False)