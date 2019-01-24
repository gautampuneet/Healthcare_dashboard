from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', views.homepage),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^Admin/', include('Admin.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
