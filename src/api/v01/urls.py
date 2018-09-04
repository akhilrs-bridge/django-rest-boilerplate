from django.conf.urls import include, url
from v01.user import urls as user_urls

urlpatterns = [
    url(r'^user/', include(user_urls)),
]
