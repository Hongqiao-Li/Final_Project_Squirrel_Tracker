from django.db import models
from django.utils.translation import gettext as _

#define our layout of our tables in our database
class Squirrel_layout(models.Model):
    longitude = models.DecimalField(
            max_digits=15,
        decimal_places = 15,
    )

# Create your models here.
