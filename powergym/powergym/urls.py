# Apenas para testar o admin
from django.contrib import admin
from django.urls import path, include

# Mudo o nome do site em si (De adminitração do site para o nome do meu site)
admin.site.site_header = "Powergym"

urlpatterns = [
    path('', include('treinos.urls')),
    path('', include('cadastro.urls')),
    #apenas para testar o admin
    path('admin/', admin.site.urls),
]