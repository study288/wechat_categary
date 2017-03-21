from django.conf.urls import url
from article import views
from pro_article import settings

urlpatterns = [

    url(r'^article/(?P<cat>\w{4})$', views.archive),

]
