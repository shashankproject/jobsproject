from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField(max_length=100);
    phonenumber=models.IntegerField();


class bangjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField(max_length=100);
    phonenumber=models.IntegerField();



class chennaijobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField(max_length=100);
    phonenumber=models.IntegerField();
