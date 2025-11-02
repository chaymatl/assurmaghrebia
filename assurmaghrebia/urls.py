# assurmaghrebia/urls.py
from django.contrib import admin
from django.urls import path, include
from sinistre.views import accueil
from django.contrib.auth import views as auth_views  
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Page d'accueil (racine)
    path('', accueil, name='accueil'),
    
    # URLs de l'application sinistre → accessible via /sinistres/
    path('sinistres/', include('sinistre.urls')),
    
    # URLs d'authentification standard (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Password Reset (mot de passe oublié)
    path('accounts/password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ), 
         name='password_reset'),
    
    path('accounts/password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('accounts/reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    
    path('accounts/reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]