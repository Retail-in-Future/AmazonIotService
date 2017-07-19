from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^things', views.index, name="get"),
}