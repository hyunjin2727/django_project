from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('word/', include('word_count.urls')),
    path('char/', include('char_count.urls')),
]