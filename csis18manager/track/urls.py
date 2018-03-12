from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'listtracks/',views.listtracks , name='listtracks'),

    ]