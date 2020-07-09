from django.contrib import admin

from .models import Ticker, Game


admin.site.register(Ticker)
admin.site.register(Game)