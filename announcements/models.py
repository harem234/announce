from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Announcement(models.Model):
    
    id = models.BigAutoField(primary_key=True, unique=True, null=False,)
    title = models.CharField(name = "title", verbose_name="titles", max_length=50, null=False, default="")
    description = models.CharField(name = "description", verbose_name="description", max_length=50, null=False, default="")
    view_count = models.IntegerField(name = "view_count", verbose_name="view_counts", null=False, default=0,)
    
    user = models.ForeignKey(name='user', to=User, on_delete=models.CASCADE)
    