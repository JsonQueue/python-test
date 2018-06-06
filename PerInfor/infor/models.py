from django.db import models


class Infor(models.Model):

    name = models.CharField(max_length=20,null=False,default='')
    job = models.CharField(max_length=20,null=False,default='')
    classmate = models.CharField(max_length=20,null=False,default='')
    home = models.CharField(max_length=100,null=False,default='')
    school = models.CharField(max_length=100,null=False,default='')
    life_info = models.TextField(max_length=100,null=False,default='')
    job_info = models.TextField(max_length=100,null=False,default='')
    classmate_info = models.TextField(max_length=100,null=False,default='')
    home_info = models.TextField(max_length=100,null=False,default='')
    school_info = models.TextField(max_length=100,null=False,default='')