from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("myprofile/<str:agent_code>/", views.profile),
    path("agents/", views.AllAgents.as_view()),
    path("profile_update/<str:agent_code>/", views.profile_update),
    path('check-auth-phone/<str:agent_code>/', views.check_auth_phone),
    path('add-auth-phone/<str:agent_code>/', views.add_agent_auth_phone),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
