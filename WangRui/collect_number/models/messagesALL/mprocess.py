# 这个表存储的是将来源，相似度合并后的数据
from django.db import models


class Process(models.Model):
    name = models.CharField(max_length=200)  # 这个message
    keyword = models.CharField(max_length=50)  # 关键词去做词云
    hot = models.IntegerField(default=100, null=True)  # 设置热度默认值为100
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'collect_number'
