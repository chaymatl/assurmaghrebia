from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sinistre.views import accueil
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Page d'accueil (racine)
    path('', accueil, name='accueil'),
    
    # Espace client
    path('espace-client/', include('espace_client.urls')),
    
    # Application sinistre
    path('sinistres/', include('sinistre.urls')),
    
    # Authentification standard (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Overrides personnalisés pour le mot de passe oublié (optionnels, mais fonctionnels)
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

# 🔧 Servir les fichiers médias (uploads) en mode développement uniquement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)