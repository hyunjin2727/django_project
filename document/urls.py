from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('word/', include('word_count.urls')),
    path('char/', include('char_count.urls')),
]


##수정 중.... 이거 적용되려나???
