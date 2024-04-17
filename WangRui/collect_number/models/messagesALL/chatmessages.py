# 这个表存储的是留言板内容
from django.db import models


class ChatMessages(models.Model):
    text = models.CharField(max_length=400)  # 这个message
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        app_label = 'collect_number'
