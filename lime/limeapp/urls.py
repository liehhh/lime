from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='limeapp-home'),
    path('register/', views.register, name='limeapp-register'),
    path('profile/', views.profile, name='limeapp-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)