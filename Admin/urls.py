from django.conf.urls import url
from . import views

app_name = 'Admin'

urlpatterns = [ 
				url(r'^$',views.admin_portal,name='admin_portal'),
]