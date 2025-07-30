# alx_travel_app/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('listings.urls')),

    # API Schema (OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # API Documentation (Swagger UI)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]