from collect_number.views.get_history import get_history
from collect_number.views.get_keyword import get_keyword
from collect_number.views.get_search import get_search
from collect_number.views.in_messages import in_messages
from collect_number.views.index import index
from collect_number.views.out_messages import out_messages
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("get_history/", get_history, name="get_history"),
    path("get_keyword/", get_keyword, name="get_keyword"),
    path("get_search/", get_search, name="get_search"),
    path("in_messages/", in_messages, name="in_messages"),
    path("out_messages/", out_messages, name="out_messages"),
]
