from django.conf.urls import url
from . import views

urlpatterns = [
    url('info/',views.info , name='info'),
    url('regsitermain/',views.registermain , name='registermain'),
    url('registertrack/',views.registertrack , name='registertrack'),
    url('deregister/',views.deregistertrack , name='deregistertrack'),
    url('listattendtrack/',views.listattendtrack , name='listattendtrack'),
    url('listmissingtrack/',views.listmissingtrack , name='listmissingtrack'),
        url('listtracks/',views.listtracks , name='listtracks'),

    ]