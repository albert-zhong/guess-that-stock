import io
import base64
import urllib
import random
import datetime
from typing import Tuple

from .tickers import get_random_ticker

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
import matplotlib.dates as mdates
import yfinance as yf


DATE_FORMAT = '%Y-%m-%d'
MIN_DATE = '2010-01-01'
MAX_DATE = '2020-06-01'
DEFAULT_INTERVAL_DAYS = 194


def get_random_date(start_date: datetime.date, end_date: datetime.date, interval: int) \
        -> Tuple[datetime.date, datetime.date]:
    """
    Returns two random dates of the given interval in days, in the form of (rnd_start_date, rnd_start_date), where
    (rnd_start_date - rnd_start_date).days = interval. Assumes that input is valid: end_date > start_date, interval > 0,
    and interval < end_date - start_date.
    """
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates - interval)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date, random_date + datetime.timedelta(days=interval)


def get_random_context():
    ticker = get_random_ticker()
    start_date, end_date = get_random_date(
        string_to_date(MIN_DATE), string_to_date(MAX_DATE), DEFAULT_INTERVAL_DAYS
    )
    start_date_string = date_to_string(start_date)
    end_date_string = date_to_string(end_date)

    data = yf.download(ticker, start_date_string, end_date_string)
    if len(data.index) < 15:
        return get_random_context()

    guessing_data = data.iloc[0:-14]['Close']
    guessing_data.plot()
    guessing_buffer = io.BytesIO()
    plot.savefig(guessing_buffer, format='png')
    guessing_buffer.seek(0)
    guessing_string = base64.b64encode(guessing_buffer.read())
    guessing_uri = urllib.parse.quote(guessing_string)
    plot.close()

    full_data = data['Close']
    full_data.plot(title=f'{ticker} Stock Price')
    before_two_weeks_date = end_date - datetime.timedelta(days=20)
    price_last_shown = data.iloc[-15]['Close']
    price_two_weeks_later = data.iloc[-1]['Close']
    color = 'green' if price_two_weeks_later > price_last_shown else 'red'
    plot.axvspan(*mdates.date2num([before_two_weeks_date, end_date]), color=color, alpha=0.5)
    full_buffer = io.BytesIO()
    plot.savefig(full_buffer, format='png')
    full_buffer.seek(0)
    full_string = base64.b64encode(full_buffer.read())
    full_uri = urllib.parse.quote(full_string)
    plot.close()

    return {
        'guessing_chart': guessing_uri,
        'full_chart': full_uri,
        'ticker': ticker,
        'price_last_shown': price_last_shown,
        'price_two_weeks_later': price_two_weeks_later,
    }


def get_uri(data, title=None):
    data.plot(title=title)
    buffer = io.BytesIO()
    plot.savefig(buffer, format='png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    plot.close()
    return uri


def string_to_date(date_string: str) -> datetime.date:
    return datetime.datetime.strptime(date_string, DATE_FORMAT).date()


def date_to_string(date: datetime.date) -> str:
    return date.strftime(DATE_FORMAT)
