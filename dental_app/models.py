from statistics import mode
from django.db import models

# Create your models here.


class patient(models.Model):
    branch=models.CharField(max_length=36, default='')
    date=models.DateField()
    first_name=models.CharField(max_length=36, default='')
    last_name=models.CharField(max_length=36, default='')
    id_number=models.IntegerField(max_length=36, default=0)
    doctor=models.CharField(max_length=36, default='')
    photo_type=models.CharField(max_length=36, default='')
    deal_number=models.IntegerField(max_length=36, default=0)
    price_type=models.CharField(max_length=36, default=0)
    credit=models.IntegerField(max_length=36, default=0)
    cash=models.IntegerField(max_length=36, default=0)
    reimbursement_from_insurance=models.IntegerField(max_length=36, default=0)
    reference_number=models.CharField(max_length=36, default=0)
    invoicing_number=models.IntegerField(max_length=36, default=0)
    way=models.CharField(max_length=36, default='')
    photographer_name=models.CharField(max_length=36, default='')

    def __str__(self):
        return self.first_name




