from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('detail/<str:pk>', views.detail, name="detail"),
    path('send_msg/<str:pk>', views.sendMsg, name="send_msg"),
    path('rcvd_msg/<str:pk>', views.recievedMsg, name="rcvd_msg"),
    path('notification', views.notification, name='notification')
]