
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #   url(r'^$',views.dashboard),
    path('', views.dashboard, name='dashboard'),
    url(r'^station/$',views.station),
    url(r'^bustation/$',views.bustation),
]
