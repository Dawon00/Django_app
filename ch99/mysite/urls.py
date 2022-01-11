from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
