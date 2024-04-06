from django.db import models
import uuid

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    is_deleted=models.BooleanField(default=False)
    class Meta:
        db_table = 'Register'
        verbose_name = ('Register')
        verbose_name_plural = ('register')

# Create your models here.
