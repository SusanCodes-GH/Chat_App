from django.shortcuts import render, redirect
from .models import Profile, Friend, Chatmsg
from .forms import Chatmsgform
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {"user":user, "friends":friends}
    return render(request, "htmlFiles/index.html", context)

def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = Chatmsg.objects.all()
    rcvd_chats = Chatmsg.objects.filter(msg_sender=profile, msg_reciever=user)
    rcvd_chats.update(seen=True)
    form = Chatmsgform()
    if request.method == "POST":
        form = Chatmsgform(request.POST)
        if form.is_valid():
            chat_msg = form.save(commit=False)
            chat_msg.msg_sender = user
            chat_msg.msg_reciever = profile
            chat_msg.save()
            return redirect("detail", pk=friend.profile.id)
    context = {"friend":friend, "form":form, "chats":chats, "user":user, "profile":profile, "num":rcvd_chats.count()}
    return render(request, "htmlFiles/detail.html", context)

def sendMsg(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    msg = data["msg"]
    chat = Chatmsg.objects.create(body=msg, msg_sender=user, msg_reciever=profile, seen=False)
    return JsonResponse(chat.body, safe=False)

def recievedMsg(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    arr = []
    chats = Chatmsg.objects.filter(msg_sender=profile, msg_reciever=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)

def notification(request):
    user = request.user.profile
    friends = user.friends.all()
    arr = []
    for friend in friends:
        chats = Chatmsg.objects.filter(msg_sender__id=friend.profile.id, msg_reciever=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)