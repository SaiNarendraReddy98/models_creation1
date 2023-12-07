from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

class AcessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True,unique=True)

class States(models.Model):
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=100,primary_key=True,unique=True)

    

