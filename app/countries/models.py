from django.db import models

class Country(models.Model):
    name = models.CharField(verbose_name = 'Name', blank = False, null = False, max_length = 255, unique = True)
    continent = models.CharField(verbose_name = 'Continent', blank = False, null = False, max_length = 255)
    acronym = models.CharField(verbose_name = 'Acronym', blank = False, null = False, max_length = 3)

    def __str__(self):
        return self.name


class HostCountry(models.Model):
    championship = models.ForeignKey('championships.Championship', verbose_name = 'Championship', null = False, blank = False, on_delete = models.PROTECT)
    country = models.ForeignKey('countries.Country', verbose_name = 'Country', null = False, blank = False, on_delete = models.PROTECT)

    def __str__(self):
        return self.country