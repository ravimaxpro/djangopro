'''
from django.db import models
from datetime import datetime

# Create your models here.
class GenAgentMaster(models.Model):
    agent_id=models.CharField(primary_key=True, max_length=20)
    agent_name = models.CharField(max_length=120,blank=True,null=True)
    agent_dob = models.DateField(blank=True,null=True)
    agent_qualification = models.CharField(max_length=120,blank=True,null=True)
    agent_join_date = models.DateField(blank=True,null=True,auto_now_add=True)
    agent_start_date = models.DateField(blank=True,null=True)
    agent_end_date = models.DateField(blank=True,null=True)
    agent_status = models.CharField(max_length=20,blank=True,null=True)
    created_by = models.CharField(max_length=120,blank=True,null=True).hidden
    created_date = models.DateField(null=True,blank=True,auto_now_add=True)
    last_updated_by = models.CharField(max_length=200,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True,auto_now_add=True)

def __str__(self):
    return self.agent_id

def get_agent_age(self):
    import datetime
    return int(((datetime.date.today() - self.agent_dob).days / 365.25))

def get_unique_id(self):
    a=self.agent_name[:2].upper() # First 2 letters of last name
    b=self.agent_dob.strftime('%d')# Day of the month as string
    c=self.agent_qualification[:2].upper()#First 2 letters of city
    d='AG-'
    return d + a + b + c

def save(self,*args,**kwargs):
    self.agent_id = self.get_unique_id
    self.agent_age = self.get_agent_age
    self.created_date = self.datetime.today()
    self.last_updated_date = self.datetime.today()
    super(GenAgentMaster, self).save(*args,**kwargs)


class genProductMaster(models.Model):
    prod_code = models.CharField(primary_key=True, max_length=200)
    prod_description = models.CharField(max_length=2000, blank=True, null=True)
    prod_start_date = models.DateField(blank=True, null=True)
    prod_end_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.prod_code

    def save(self):
        if not self.prod_code:
            self.created_date= self.datetime.today()
            self.last_update_date=self.datetime.today()
            super(genProductMaster, self).save()
'''





