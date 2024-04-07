from django.contrib import admin
from django.urls import path, re_path, include,path
from django.views.static import serve
from django.conf import settings
from referral import views
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/general/',include('api.v1.general.urls',namespace='api_v1_general')),
    path('api/v1/referral/', include('api.v1.referral.urls', namespace='api_v1_referral')),
   
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
