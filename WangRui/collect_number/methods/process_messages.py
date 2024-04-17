import os

import django
import torch
from django.conf import settings
from django.utils import timezone
from transformers import BertTokenizer, BertModel

# 设置 DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collect_number.settings")

# 调用 settings.configure()
settings.configure()

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'messages',
        'USER': 'root',
        'PASSWORD': 'wr1234567890',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

django.setup()

from WangRui.collect_number.models.messagesALL.messagesALL import MessagesALL
from WangRui.collect_number.models.messagesALL.mprocess import Process

today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
today_end = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)

# 初始化模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-chinese')


# 判断两个句子的相似度
def is_same_thing_bert(sentence1, sentence2, threshold=0.75):
    # 分词并编码句子
    inputs = tokenizer([sentence1, sentence2], return_tensors='pt', padding=True, truncation=True)

    # 通过模型获取句子的嵌入向量
    with torch.no_grad():
        outputs = model(**inputs)

    # 使用平均池化获取句子的嵌入表示
    embeddings = outputs.last_hidden_state.mean(dim=1)

    # 计算余弦相似度
    cos = torch.nn.CosineSimilarity(dim=0)
    similarity = cos(embeddings[0], embeddings[1]).item()

    # 判断是否相同
    return similarity > threshold


# 判断keyword是否是包涵关系
def has_common_keyword(keyword1, keyword2):
    words1 = set(keyword1.split(','))  # 将字符串分割成词的集合
    words2 = set(keyword2.split(','))
    return not words1.isdisjoint(words2)  # 检查是否有共同的词


# 删除day天前的数据
def delete_old_data(day):
    ten_days_ago = timezone.now() - timezone.timedelta(days=day)
    Process.objects.filter(created_at__lt=ten_days_ago).delete()


# 获取当天的所有数据
records = MessagesALL.objects.filter(created_at__range=(today_start, today_end))
results = []

if __name__ == '__main__':
    delete_old_data(10)

    # 创建一个临时存储以合并数据
    for i in range(len(records)):
        merged = False
        for result in results:
            if has_common_keyword(records[i].keyword, result['keyword']) and is_same_thing_bert(records[i].name,
                                                                                                result['name']):
                result['hot'] += records[i].hot
                merged = True
                break
        if not merged:
            results.append({'name': records[i].name, 'keyword': records[i].keyword, 'hot': records[i].hot})

    for result in results:
        new_record = Process(name=result['name'], keyword=result['keyword'], hot=result['hot'])
        new_record.save()
