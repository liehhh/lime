from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .forms import LimeLoginForm
from . import views


urlpatterns = [
    path('', views.home, name='limeapp-home'),
    path('profile/', views.profile, name='limeapp-profile'),

    path('register/', RegisterView.as_view(), name='register'),

    path('login/', auth_views.LoginView.as_view(authentication_form=LimeLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)