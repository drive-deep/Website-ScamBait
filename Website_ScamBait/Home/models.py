from django.db import models

# Create your models here.
class scam(models.Model):
    account_no = models.CharField(max_length=20, default='', null=False)
    inlineRadioOptions = models.CharField(max_length=20, default='', null=False)
    online = models.CharField(max_length=20, default='on', null=True)
    offline = models.CharField(max_length=20, default='', null=True)
    phone = models.CharField(max_length=20, default='', null=False, primary_key=True)
    upi_id = models.CharField(max_length=20, default='', null=False)
