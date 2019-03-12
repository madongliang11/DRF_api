
from django.conf.urls import url, include
from django.contrib import admin

from main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',namespace="api")),
    url(r"getusershoes/",views.get_user_shoes),
    url(r"updateusershoes/",views.update_user_shoes),
]
