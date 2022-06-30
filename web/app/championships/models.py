from django.db import models

class Championship(models.Model):
    year = models.CharField(unique = True, verbose_name = 'Year', max_length = 4, null = False, blank = False)
    total_countries = models.IntegerField(verbose_name = 'Total Countries', null = False, blank = False)
    total_goals = models.IntegerField(verbose_name = 'Total Goals', null = False, blank = False)
    total_audience = models.IntegerField(verbose_name = 'Total Audience', null = False, blank = False)
    golden_ball = models.ForeignKey('players.Player', related_name = '%(class)s_golden_ball', verbose_name = 'Golden Ball', null = True, blank = True, on_delete = models.PROTECT)
    golden_boot = models.ForeignKey('players.Player', related_name = '%(class)s_golden_boot', verbose_name = "Golden Boot", null = True, blank = True, on_delete = models.PROTECT)
    golden_glove = models.ForeignKey('players.Player', related_name = '%(class)s_golden_glove', verbose_name = 'Golden Glove', null = True, blank = True, on_delete = models.PROTECT)

    def __str__(self):
        return self.year

