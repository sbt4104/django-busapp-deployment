from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    start_stop = models.CharField(max_length=128)
    end_stop = models.CharField(max_length=128)
    amount = models.IntegerField(max_length=254,unique=False)
    timec = models.TimeField(default= datetime.today)
    seats = models.IntegerField(unique=False)
    total_peo = models.IntegerField(unique=False)
'''
class User(models.Model):
    start_stop = models.CharField(max_length=128)
    end_stop = models.CharField(max_length=128)

'''

'''class stop_details(models.Model):
   s1 = models.CharField(max_length=256)
   s2 = models.CharField(max_length=128)
   time = models.TimeField()
   amt = models.IntegerField()

   # other fields, etc...

   #friends = models.ManyToManyField('self')

class Bus_details(models.Model):
   Bus_name = models.CharField(max_length=256)
   stp_details = models.ManyToManyField(stop_details)
'''

class Notifi(models.Model):
    stop_name = models.CharField(max_length=128)


class Bar(models.Model):
    bus_no = models.IntegerField(unique=False)
    total_no_of_stops = models.IntegerField(unique=False)
    enter_stop_price_time_with_commas = models.TextField(blank=True)
    enter_time = models.TextField(blank=True)

    def set_list(self, element):
        if self.foo:
            self.foo = self.foo + "," + element
        else:
            self.foo = element

    def get_list(self):
        if self.foo:
            return self.foo.split(",")
        else:
            None

class ML_data(models.Model):
    accidents = models.IntegerField(unique=False)
    vechile_breakdown = models.IntegerField(unique=False)
    weather = models.TextField(blank=False)
    Traffic = models.IntegerField(unique=False)
    route = models.IntegerField(unique=False)
    density = models.IntegerField(unique=False)
    time_of_day = models.TimeField(unique=False,default= datetime.today)
    delay = models.TimeField(unique=False,default='20:00')
