from collect_number.models.messagesALL.chatmessages import ChatMessages
from django.http import JsonResponse


def in_messages(request):
    data = request.GET
    print(data)
    text = data.get("text", "").strip()
    ChatMessages.objects.create(text=text)
    return JsonResponse({
        'result': "success",
    })
