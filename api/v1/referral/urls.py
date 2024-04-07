from django.urls import path
from api.v1.referral import views

app_name = "api_v1_referral"

urlpatterns =[
    path('register-user/',views.register_user),
    path('view-details/<pk>',views.view_details),
    path('view-referral-data/<pk>',views.view_referral_data),

]