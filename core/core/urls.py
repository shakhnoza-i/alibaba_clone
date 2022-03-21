from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('post_cart/', include('cart.urls')),
    path('post_review/', include('review.urls')),
    path('account/', include('user_app.urls')),
    path('companies/', include('companies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
