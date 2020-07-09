from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

import datetime


class Ticker(models.Model):
    symbol = models.CharField(max_length=5)
    chart = MatplotlibFigureField()
    price_did_rise = models.BooleanField()

    def __str__(self):
        return self.symbol


class Game(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.ticker}, {self.start_date} to {self.end_date}'

    def two_weeks_later(self):
        return self.end_date + datetime.timedelta(days=14)

