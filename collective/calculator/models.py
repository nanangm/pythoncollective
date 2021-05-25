from django.db import models
from django.urls import reverse

from django.db import connections
import sqlite3

conn = sqlite3.connect('db.sqlite3')
 
# Create your models here.
class calculator(models.Model):
    tally = models.CharField(primary_key=True, max_length=15)
    result = models.CharField(max_length=15)


    class Meta:
        db_table="calculator"
    
    
    def __str__(self):
        return self.tally

    def save(self): # ALL the signature
        super(calculator, self).save(using='calculator')