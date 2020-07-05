from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/v1/', include('channels.api_urls')),
    path(settings.ADMIN_PATH, admin.site.urls),
    path(r'login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('channels.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
