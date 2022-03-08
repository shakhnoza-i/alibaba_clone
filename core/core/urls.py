from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('account/', include('user_app.urls')),
    path('companies/', include('companies.urls')),
]
