# 获取总数据
import os
import re

import django
import jieba.analyse
import requests
from django.conf import settings
from django.utils import timezone

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

urls = [
    'https://tenapi.cn/v2/baiduhot',   # 百度热搜榜
    'https://tenapi.cn/v2/douyinhot',  # 抖音热搜榜
    'https://tenapi.cn/v2/weibohot',   # 微博热搜榜
    'https://tenapi.cn/v2/zhihuhot',   # 知乎热搜榜
]
sources = ['baidu', 'douyin', 'weibo', 'zhihu']


# 提取热度中的数字
def extract_last_integer_from_string(input_string):
    # 使用正则表达式找到所有包含数字的子串
    matches = re.findall(r'\d+', input_string)
    if matches:
        # 提取最后一个匹配到的数字并转换为整数
        extracted_number = int(matches[-1])
        return extracted_number
    else:
        # 没有找到数字
        return 0


# 从api获取数据写入数据库
def data_in_model(index, my_url):
    response = requests.get(my_url)
    if response.status_code == 200:
        # 解析JSON数据
        json_data = response.json().get('data')
        if json_data is not None:
            # 将数据写入总表中
            for data in json_data:
                name = data.get('name')
                keyword = jieba.analyse.extract_tags(name,
                                                     topK=2, allowPOS=('n', 'nr', 'ns'))
                hot = extract_last_integer_from_string(data.get('hot'))
                source_url = data.get('url')
                source = sources[index]
                MessagesALL.objects.create(name=name, keyword=keyword, hot=hot, url=source_url, source=source)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


# 删除day天前的数据
def delete_old_data(day):
    ten_days_ago = timezone.now() - timezone.timedelta(days=day)
    MessagesALL.objects.filter(created_at__lt=ten_days_ago).delete()


if __name__ == '__main__':
    # 删除十天前的数据
    delete_old_data(10)
    # 将数据写入数据库
    for n, url in enumerate(urls):
        data_in_model(n, url)


    # while True:
    #     time_now = time.strftime("%H%M", time.localtime())  # 刷新
    #     if time_now == "10:00":
    #         for n, url in enumerate(urls):
    #             data_in_model(n, url)
    #         delete_old_data(10)
