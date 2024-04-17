from django.db import models


class MessagesALL(models.Model):
    name = models.CharField(max_length=200)  # 这个message
    keyword = models.CharField(max_length=50)  # 关键词
    hot = models.IntegerField(default=100, null=True)  # 设置热度默认值为100
    url = models.URLField(max_length=256)  # 这个message的url
    source = models.CharField(max_length=20)  # 来自哪个平台
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'collect_number'
