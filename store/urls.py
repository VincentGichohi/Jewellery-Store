from django.urls import path
from store.forms import LoginForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from . import views
from django.contrib.auth import views as auth_views
