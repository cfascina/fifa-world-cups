from django.contrib import admin

from .models import Game, Card, Phase

admin.site.register(Game)
admin.site.register(Card)
admin.site.register(Phase)