from django.db import models

class Player(models.Model):
    name = models.CharField(verbose_name = 'Name', null = False, blank = False, max_length = 255)
    tshirt_name = models.CharField(verbose_name = 'T-shirt Name', null = False, blank = False, max_length = 255)
    birth_date = models.DateField(verbose_name = 'Birth Date', null = False, blank = False)
    country = models.ForeignKey('countries.Country', verbose_name = 'Country', null = False, blank = False, on_delete = models.PROTECT)

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = Player