from django.db import models

class Phase(models.Model):
    name = models.CharField(verbose_name = 'Name', null = False, blank = False, max_length = 255)

    def __str__(self):
        return self.name


