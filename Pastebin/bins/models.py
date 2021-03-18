from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
    Transform,
)
from django.db.models.lookups import (
    YearExact, YearGt, YearGte, YearLt, YearLte,
)
from django.utils import timezone

#User = settings.AUTH_USER_MODEL 

 #Create your models here.

class Binss(models.Model):
	user 	 = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='Binss')
	title 	 = models.CharField(max_length=100, null=False)
	text     = models.TextField(null=False)
	bin_date = models.DateTimeField(default=timezone.now)

	



