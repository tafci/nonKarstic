from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls', namespace='common')),
    path('cave/', include('map_viewer.urls', namespace='cave')),
]
