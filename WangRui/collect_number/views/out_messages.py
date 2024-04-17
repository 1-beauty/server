from collect_number.models.messagesALL.chatmessages import ChatMessages
from django.http import JsonResponse


def out_messages(request):
    data = request.GET
    datas = []
    messages = ChatMessages.objects.filter().order_by('created_at')[:20]
    for item in messages:
        if item.text != '':
            datas.append({
                'text': item.text,
            })

    return JsonResponse({
        'result': "success",
        'data': datas,
    })
