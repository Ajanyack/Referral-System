from django.db.models import *
from random import randint
from django.contrib.auth.models import User

import random
import string
from django.conf import settings



def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        # message += "%s : %s | " %(key,error_message)
        message += f"{key} - {error_message} | "
    return message[:-3]


def randomnumber(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1

    return randint(range_start, range_end)


def check_username(username):
    old_username = username
    if User.objects.filter(Q(username__icontains=username)).exists():
        print(username, "========old===========")
        sliced_phone = username[3:7]
        new_random_number = randomnumber(4)
        new_username = f'EZG{sliced_phone}{new_random_number}'
        print(new_username, "========new===========")
        check_username(new_username)
        return new_username
    else:
        return old_username
    
