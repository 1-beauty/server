from collect_number.models.messagesALL.messagesALL import MessagesALL
from django.http import JsonResponse
from django.utils.timezone import localtime


def get_history(request):
    query_string = request.GET.get('query', '')
    records = MessagesALL.objects.filter(name__icontains=query_string)

    # 用Python处理日期分组，而不是在数据库级别处理
    data = {}
    for record in records:
        date_key = localtime(record.created_at).date()
        if date_key not in data:
            data[date_key] = record.hot
        else:
            data[date_key] += record.hot

    # 转换成期望的格式
    result = [{"date": key, "total_hot": value} for key, value in data.items()]
    return JsonResponse({
        'result': 'success',
        'data':result,
    })
