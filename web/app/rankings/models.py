from django.db import models

class Ranking(models.Model):
    championship = models.ForeignKey('championships.Championship',  verbose_name = "Championship", null = False, blank = False, on_delete = models.PROTECT)
    country = models.ForeignKey('countries.Country',  verbose_name = 'Country', null = False, blank = False, on_delete = models.PROTECT)
    position = models.IntegerField(verbose_name = 'Position', null = False, blank = False)

    def __str__(self):
        return self.championship