from django.db import models 


CARD_COLORS = (
    ('Y', 'YELLOW'),
    ('R', 'RED')
)

class Game(models.Model): 
    goals_country_home = models.IntegerField(verbose_name = 'Goals Country Home', null = False, blank = False)
    goals_country_guest = models.IntegerField(verbose_name = 'Goals Country Guest', null = False, blank = False)
    tickets = models.IntegerField(verbose_name = 'Tickets', null = False, blank = False)
    audience = models.IntegerField(verbose_name = 'Audience', null = False, blank = False)
    date = models.DateTimeField(verbose_name = 'Date', null = False, blank = False)
    win_condition = models.CharField(verbose_name = 'Winner Condition', null = True, blank = True, max_length = 255)
    championship = models.ForeignKey('championships.Championship', verbose_name = "Championship", null = False, blank = False, on_delete = models.PROTECT)
    phase = models.ForeignKey('Phase', verbose_name = 'Phase', null = False, blank = False, on_delete = models.PROTECT)
    country_home = models.ForeignKey('countries.Country', related_name = '%(class)s_country_home', verbose_name = 'Country Home', null = False, blank = False, on_delete = models.PROTECT)
    country_guest = models.ForeignKey('countries.Country', related_name = '%(class)s_country_guest', verbose_name = 'Country Guest', null = False, blank = False, on_delete = models.PROTECT)
    stadium = models.ForeignKey('stadiums.Stadium', verbose_name = 'Stadium', null = False, blank = False, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.country_home} ({self.goals_country_home}) vs. ({self.goals_country_guest}) {self.country_guest}"

class Card(models.Model):
    color = models.CharField(verbose_name = 'Color', null = True, blank = True, choices = CARD_COLORS, max_length = 6)
    game = models.ForeignKey('Game', verbose_name = 'Game', null = False, blank = False, on_delete = models.PROTECT)
    player = models.ForeignKey('players.Player', verbose_name = 'Player', null = False, blank = False, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.player} ({self.color})" 
    
class Phase(models.Model):
    name = models.CharField(verbose_name = 'Name', null = False, blank = False, max_length = 255)
    
    def __str__(self):
        return self.name