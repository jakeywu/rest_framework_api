from django.conf.urls import url
from learn_rest_framework.views import PublicWechat
urlpatterns = [
    url(r'^api/weixin$', PublicWechat.as_view(), name='wechat'),
]
