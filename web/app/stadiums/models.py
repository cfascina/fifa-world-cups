from django.db import models

class Stadium(models.Model):
    name = models.CharField(verbose_name = 'Name', null = False, blank = False, max_length = 255)
    city = models.CharField(verbose_name = 'City', null = False, blank = False, max_length = 255)
    capacity = models.IntegerField(verbose_name = 'Capacity', null = True, blank = False)
    country = models.ForeignKey('countries.Country', verbose_name = 'Country', null = False, blank = False, on_delete = models.PROTECT)

    def __str__(self):
        return self.name

