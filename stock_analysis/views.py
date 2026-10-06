"""
Stock Analysis views.

Data is loaded once at module level from a .feather file so each request
doesn't re-read disk. The cache layer adds another guard in production.
"""

import json

import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render

# ---------------------------------------------------------------------------
# Module-level data load — runs once per worker process
# ---------------------------------------------------------------------------
_DATA_FILE = settings.BASE_DIR / 'data' / 'stocks.feather'

try:
    _STOCKS_DF = pd.read_feather(_DATA_FILE)
except FileNotFoundError:
    # Provide a minimal demo dataset so the view doesn't crash during dev
    _STOCKS_DF = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30, freq='B'),
        'ticker': ['DEMO'] * 30,
        'close': [100 + i * 0.5 for i in range(30)],
        'volume': [1_000_000] * 30,
    })


def index(request):
    """Overview: list of available tickers."""
    tickers = sorted(_STOCKS_DF['ticker'].unique().tolist())
    return render(request, 'stock_analysis/index.html', {'tickers': tickers})


def detail(request, ticker):
    """Candlestick / line chart for a single ticker."""
    cache_key = f'stock_chart_{ticker}'
    chart_data = cache.get(cache_key)

    if chart_data is None:
        df = _STOCKS_DF[_STOCKS_DF['ticker'] == ticker].copy()
        df = df.sort_values('date')
        chart_data = {
            'dates':  df['date'].dt.strftime('%Y-%m-%d').tolist(),
            'closes': df['close'].tolist(),
        }
        cache.set(cache_key, chart_data, timeout=60 * 15)  # 15 min

    context = {
        'ticker': ticker,
        'chart_json': json.dumps(chart_data),
    }
    return render(request, 'stock_analysis/detail.html', context)
