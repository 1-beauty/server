from collect_number.models.messagesALL.mprocess import Process
from django.http import JsonResponse


def get_keyword(request):
    datas = []

    words = Process.objects.filter().order_by('hot')[:50]
    for item in words:
        if item.keyword != '[]':
            datas.append({
                'name': item.name,
                'word':item.keyword.strip("[]"),
                'hot': item.hot,
            })
    return JsonResponse({
        'result': "success",
        'data': datas,
    })
