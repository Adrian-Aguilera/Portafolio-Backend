"""
URL configuration for portafolio_Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import index

schema_view = get_schema_view(
   openapi.Info(
      title="API Portafolio Adrian Aguilera",
      default_version='v1',
      description="Documentación de API para el proyecto Portafolio",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="adrian.aguileragcm@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('Portafolio_App.urls')),
    path('tokens/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #rutas de swagger:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
