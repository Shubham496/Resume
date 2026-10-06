"""
ML Demo views.

Heavy model outputs are precomputed at module level (or cached) rather than
re-running on every request.
"""

import json

import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render

# ---------------------------------------------------------------------------
# Module-level: precompute demo predictions once
# ---------------------------------------------------------------------------
_DATA_FILE = settings.BASE_DIR / 'data' / 'ml_results.feather'

try:
    _RESULTS_DF = pd.read_feather(_DATA_FILE)
except FileNotFoundError:
    # Minimal demo dataset
    import numpy as np
    rng = np.random.default_rng(42)
    n = 50
    _RESULTS_DF = pd.DataFrame({
        'feature_1': rng.normal(size=n).round(3),
        'feature_2': rng.normal(size=n).round(3),
        'actual':    rng.integers(0, 2, size=n),
        'predicted': rng.integers(0, 2, size=n),
        'probability': rng.uniform(0, 1, size=n).round(3),
    })


def index(request):
    """ML demo overview / scatter plot."""
    cache_key = 'ml_scatter'
    scatter_data = cache.get(cache_key)

    if scatter_data is None:
        df = _RESULTS_DF
        scatter_data = {
            'x':     df['feature_1'].tolist(),
            'y':     df['feature_2'].tolist(),
            'label': df['actual'].tolist(),
        }
        cache.set(cache_key, scatter_data, timeout=60 * 60)  # 1 hour

    accuracy = (
        (_RESULTS_DF['actual'] == _RESULTS_DF['predicted']).sum()
        / len(_RESULTS_DF)
        * 100
    )

    context = {
        'scatter_json': json.dumps(scatter_data),
        'accuracy': round(accuracy, 1),
        'n_samples': len(_RESULTS_DF),
    }
    return render(request, 'ml_demo/index.html', context)
