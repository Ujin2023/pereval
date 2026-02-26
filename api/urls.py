from django.urls import path
from .views import SubmitDataView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('submit/', SubmitDataView.as_view(), name='submit'),
    path('submit/<int:pk>/', SubmitDataView.as_view(), name='submitperone'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Путь к Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Путь к ReDoc (альтернативный вид документации)
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]