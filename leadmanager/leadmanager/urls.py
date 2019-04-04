from django.contrib import admin
from django.urls import path, include

print(include('leads.urls'))
urlpatterns = [
    path('', include('leads.urls')),
    path('admin/', admin.site.urls),
]
