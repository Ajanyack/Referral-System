from django.contrib import admin
from django.urls import path, re_path, include,path
from django.views.static import serve
from django.conf import settings
from referral import views


urlpatterns = [
    path('admin/', admin.site.urls),
   
    
    path('api/v1/referral/', include('api.v1.referral.urls', namespace='api_v1_referral')),
   
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
