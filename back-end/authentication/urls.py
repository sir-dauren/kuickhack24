from django.urls import path
from .views import auth, profile

urlpatterns = [
    path('sign-up/', auth.sign_up, name='sign-up'),
    path('sign-in/', auth.sign_in, name='sign-in'),
    path('sign-out/', auth.sign_out, name='sign-out'),

    path('profile/', profile.profile, name='profile'),
]
