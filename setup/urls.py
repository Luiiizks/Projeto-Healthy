from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('healthy.urls')),
    path('goals/', include('goals.urls')),

    path('treino/', include('treino.urls')),
    path('dieta/', include('dieta.urls', namespace='dieta')),
    path('calculos/', include('calculos.urls', namespace='calculos')),
    path('registro/', include('registro.urls')),

    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
