from django.db import models
from django.core.validators import RegexValidator

class Card(models.Model):
    # validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # fields
    first_last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, default='')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    photo = models.FileField(upload_to='photo', blank=True, null=True)
    vcard_address = models.CharField(max_length=255, blank=True, default='')


    def __str__(self) -> str:
        return f'{self.first_last_name} ({self.pk})'