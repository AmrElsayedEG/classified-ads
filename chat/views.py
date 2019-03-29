from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import chat
from .forms import chatForm
from .models import chat
from accounts.models import Profile
from notify.signals import notify
# Create your views here.
def chatHome(request,name):
    u = request.user
    rec_img = get_object_or_404(Profile, slug=name)
    sen_img = get_object_or_404(Profile, slug=u)
    messages = chat.objects.filter(sender__username=request.user,receiver__username=name)
    messages_1 = chat.objects.filter(sender__username=name,receiver__username=request.user)
    us = User.objects.get(username=name)
    print(rec_img.img)
    list = []
    list_1 = []
    list_2 = []
    for i in messages:
        list_1.append(i.id)
        list.append(i.id)
    for i in messages_1:
        list_2.append(i.id)
        list.append(i.id)
    list.sort()
    msg_list = {}
    for i in list:
        if i in list_1:
            for x in messages:
                if x.id == i:
                    msg_list.update({x.message:x.sender})
        elif i in list_2:
            for x in messages_1:
                if x.id == i:
                    msg_list.update({x.message:x.sender})
    chat_form = chatForm()
    if request.method == 'POST':
        chat_form = chatForm(request.POST)
        if chat_form.is_valid():
            m = chat()
            m.sender = request.user
            m.receiver = us
            m.message = chat_form.cleaned_data['message']
            m.save()
            notify.send(request.user, recipient=us, actor=request.user,verb='sent you a message', nf_type='followed_by_one_user')
    else:
        chat_form = chatForm()
    # get_object_or_404(chat,receiver=pk)

    context = {
        'chat_form':chat_form,
        'msg_list': msg_list,
        'rec_img':rec_img,
        'sen_img':sen_img,
        'u':u,
        'name':name
    }
    return render(request,'chat.html',context)