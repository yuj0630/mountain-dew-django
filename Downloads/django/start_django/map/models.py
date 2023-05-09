from django.db import models
 
# Create your models here.
class pmntn(models.Model):
    PMNTN_SN = models.IntegerField(max_length=10, primary_key=True)
    MNTN_CODE = models.CharField(max_length=9, null=False)
    MNTN_NM = models.CharField(max_length=50, null=False)
    PMNTN_NM = models.CharField(max_length=50)
    PMNTN_MAIN = models.CharField(max_length=200)
    PMNTN_LT = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    PMNTN_DFFL = models.CharField(max_length=8)
    PMNTN_UPPL = models.IntegerField(max_length=10)
    PMNTN_GODN = models.IntegerField(max_length=10)
    PMNTN_MTRQ = models.CharField(max_length=200)
    PMNTN_CRNL = models.CharField(max_length=1)
    PMNTN_CLS_ = models.CharField(max_length=1)
    PMNTN_RISK = models.CharField(max_length=200)
    PMNTN_RECO = models.CharField(max_length=1)

class gpx_data(models.Model):
    id = models.IntegerField(max_length=50)
    file_name = models.CharField(max_length=200)
    xml_data = models.TextField()
