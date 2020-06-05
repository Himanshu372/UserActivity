from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=9, null=False, unique=True)
    real_name = models.CharField(max_length=50, null=False)
    timezone = models.CharField(max_length=100, null=False)

class activity_period(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=user, on_delete=models.CASCADE, to_field='user_id', null=False)
    start_time = models.CharField(max_length=25, null=False)
    end_time = models.CharField(max_length=25, null=False)

