"""
portfolio_hub URL configuration
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',           include('portfolio.urls')),
    path('stocks/',    include('stock_analysis.urls')),
    path('ml/',        include('ml_demo.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
