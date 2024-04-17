from collect_number.models.messagesALL.messagesALL import MessagesALL
from django.db.models.functions import TruncDate
from django.http import JsonResponse


def get_search(request):
    query = request.GET.get('query', '')
    if query:
        results = MessagesALL.objects.filter(name__icontains=query)
        results = results.annotate(date_only=TruncDate('created_at')).order_by('-date_only', '-hot')
    else:
        results = MessagesALL.objects.none()  # 如果没有查询字符串，则返回空查询集

    # 将结果转换为字典列表
    data = list(results.values('name', 'created_at', 'hot', 'id', 'keyword', 'source', 'url'))

    return JsonResponse(data, safe=False)  # 返回 JSON 数据
