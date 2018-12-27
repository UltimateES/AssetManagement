from django.db import models
import time
# Create your models here.


def get_resume_folder(instance, filename):
    return "maintainance/%s/%s" %(instance,int(time.time()))
    # store image with unique timestamp in filename for eg: 224355432_team1.jpg

def get_qr_code(instance, filename):
    return "qrcode/%s/%s" %(instance,int(time.time()))

class Asset(models.Model):
    """docstring for Asset."""

    asset_name = models.CharField(max_length=200,blank=False)
    asset_location = models.CharField(max_length=200,blank=False)
    asset_supplied_by = models.CharField(max_length=200,blank=False)
    asset_installation_date = models.DateField(max_length=200,blank=False)
    asset_commissioning_date = models.DateField(max_length=200,blank=False)
    asset_manufactured_by = models.CharField(max_length=200,blank=False)
    asset_warranty_expiration_date = models.DateField(max_length=200,blank=False)
    asset_overhauling_date = models.DateField(max_length=200,blank=False)
    asset_codallife_date = models.DateField(max_length=200,blank=False)
    asset_maintainance_procedure = models.FileField(upload_to=get_resume_folder,blank=True)
    asset_mainatainance_history = models.CharField(max_length=500,blank=False)
    asset_test_procedure = models.FileField(upload_to=get_resume_folder,blank=True)
    #qr_code = models.FileField(upload_to=get_qr_code,blank=True,null=True)


    def __str__(self):
        return self.asset_name
