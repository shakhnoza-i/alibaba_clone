from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('cart/', include('cart.urls')),
    path('post/', include('review.urls')),
    path('account/', include('user_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
