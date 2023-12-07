from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
        return self.name

class AcessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.author

class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True,unique=True)
    capital_name=models.CharField(max_length=100)
    def __str__(self):
        return self.country_name
    

class State(models.Model):
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=100,primary_key=True,unique=True)
    city_name=models.CharField(max_length=100)
    def __str__(self):
        return self.state_name

    

