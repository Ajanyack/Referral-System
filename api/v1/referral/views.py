import traceback

from django.db import transaction
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from referral.models import *
from general.decorators import group_required
from general.functions import generate_serializer_errors, get_auto_id
from api.v1.referral.serializers import *
from django.conf import settings
from django.template.loader import get_template


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        transaction.set_autocommit(False)
        serialized_data = CreateRegisterSerializer(data = request.data)
        if serialized_data.is_valid():
            name = request.data["name"]
            email = request.data["email"]
            password = request.data["password"]
            referral_code = request.data.get("referral_code")

            if not Register.objects.filter(name=name,email=email, is_deleted=False).exists():

                reg = Register.objects.create(
                    auto_id = get_auto_id(Register),
                    name = name,
                    email = email,
                    password = password,
                    referral_code = referral_code
                )

                password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")
                username = f'Ref{randomnumber(4)}'
                username = check_username(username)
                headers = {
                        "Content-Type": "application/json"
                    }
                data={
                        "username": username,
                        "password": password,
                    }
                
                user = User.objects.create_user(
                                username=username,
                                password=password
                            ) 
                reg.user = user
                reg.username = username
                reg.password = password                  
                reg.save()
                transaction.commit()
                student_group, created = Group.objects.get_or_create(name='registered_user')
                student_group.user_set.add(user)
                protocol = "http://"
                if request.is_secure():
                    protocol = "https://"

                host = request.get_host()

                url = protocol + host + "/api/token/"
                response = requests.post(url, headers=headers, data=json.dumps(data))
                if response.status_code == 200:
                        response = response.json()
                        response_data={
                        "StatusCode" : 6000,
                        "data":{
                            "title":"Success",
                            "Message":"Registered Successfully ",
                            "userid":reg.id,
                            "access_token" : response["access"],
                            "refresh_token" : response["refresh"],

                        }
                    } 
                
            else:
                response_data = {
                    "StatusCode" : 6001,
                    "data" : {
                        "title" : "Failed",
                        "message" : "already exists"
                    }
                }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : generate_serializer_errors(serialized_data._errors)
                }
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "status": 0,
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)

