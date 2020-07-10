from django.db import models

import datetime
import yfinance as yf


class Ticker(models.Model):
    symbol = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.symbol


class Game(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    first_chart = models.BinaryField()
    second_chart = models.BinaryField()
    price_did_rise = models.BooleanField()

    def __str__(self):
        return f'{self.ticker}, {self.start_date} to {self.end_date}'

    def two_weeks_later(self):
        return self.end_date + datetime.timedelta(days=14)

    @staticmethod
    def create_game(symbol, start_date, end_date):
        ticker = Ticker.objects.get_or_create(symbol)
        data = yf.download(symbol, start_date, end_date)





