from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'info/',views.info , name='info'),
    url(r'regsitermain/',views.registermain , name='registermain'),
    url(r'registertrack/',views.registertrack , name='registertrack'),
    url(r'deregistertrack/',views.deregistertrack , name='deregistertrack'),
    url(r'listattendtrack/',views.listattendtrack , name='listattendtrack'),
    url(r'listmissingtrack/',views.listmissingtrack , name='listmissingtrack'),
    ]