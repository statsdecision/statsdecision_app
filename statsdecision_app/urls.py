from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from django.shortcuts import redirect
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomPasswordResetView, PasswordResetCompleteView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

#app_name = 'myapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('contact', views.contact_view, name='contact'),
    path('video_list', views.resource_center, name='video_list'),
    path('Evennement', views.Evennement, name='Evennement'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('password_reset_confirm/', CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/complete/',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('reset/done/',CustomPasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

# 📌 Permet de servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


