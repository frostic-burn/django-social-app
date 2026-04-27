from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('follow-user/', views.follow_user, name='follow-user'),
	path('unfollow-user/', views.unfollow_user, name='unfollow-user'),
	path('sub-user/', views.add_subscription, name='sub-user'),
	path('unsub-user/', views.cancel_subscription, name='unsub-user'),
    path('get-data/', views.get_data, name='get_data'),
    path('my-feed/', views.my_feed, name='my-feed'),  
]
