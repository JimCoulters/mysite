from django.shortcuts import render
from .models import Station,BuStation

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def dashboard(request):
    return render(request, 'stu_crm/dashboard.html')

def station(request):
    Station.objects.filter(projectname='').delete()
    stations = Station.objects.all()

# Create your views here.
    paginator=Paginator(stations,10)    #每页显示10条
    page=request.GET.get('page')        #前段请求的页,比如点击'下一页',该页以变量'page'表示
    try:
      station_obj=paginator.page(page) #获取前端请求的页数
    except PageNotAnInteger:
        station_obj=paginator.page(1)   #如果前端输入的不是数字,就返回第一页
    except EmptyPage:
        station_obj=paginator.page(paginator.num_pages)   #如果前端请求的页码超出范围,则显示最后一页.获取总页数,返回最后一页.比如共10页,则返回第10页.
    return render(request,'stu_crm/stations.html',{'station_list':station_obj})

def bustation(request):
    BuStation.objects.filter(projectname='').delete()
    bustations = BuStation.objects.all()

# Create your views here.
    paginator=Paginator(bustations,10)    #每页显示10条
    page=request.GET.get('page')        #前段请求的页,比如点击'下一页',该页以变量'page'表示
    try:
      station_obj=paginator.page(page) #获取前端请求的页数
    except PageNotAnInteger:
        station_obj=paginator.page(1)   #如果前端输入的不是数字,就返回第一页
    except EmptyPage:
        station_obj=paginator.page(paginator.num_pages)   #如果前端请求的页码超出范围,则显示最后一页.获取总页数,返回最后一页.比如共10页,则返回第10页.
    return render(request,'stu_crm/bustations.html',{'bustation_list':station_obj})
