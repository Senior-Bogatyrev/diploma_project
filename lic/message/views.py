from django.shortcuts import render

def message_list(request):
    return render(request, 'message/message_list.html')
