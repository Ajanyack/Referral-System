from django.urls import path
from api.v1.referral import views

app_name = "api_v1_referral"

urlpatterns =[
    path('register-user/',views.register_user),
   

]