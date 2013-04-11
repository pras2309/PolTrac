from django.db import models

# Create your models here.
class User(models.Model):
    
    def __unicode__(self):
        return self.username
        
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    
    