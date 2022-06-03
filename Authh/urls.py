from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    ## Homepage
    path('', dashboard, name='dashboard'),
    ## login, logout ,register
    path('login/',login_user, name='login'),
    path('logoutuser/', logoutUser, name="logoutuser"),
    path('registerUser/', registerUser, name='registeruser'),

    ## Forgot Password Email

    path('reset_pasword/', auth_views.PasswordResetView.as_view(
        template_name="auth/reset_password.html"), name="reset_pasword"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="auth/reset_password_send.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/reset_password_complete.html"), name="password_reset_complete"),

]