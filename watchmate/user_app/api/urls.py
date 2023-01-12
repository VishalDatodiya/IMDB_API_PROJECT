from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from user_app.api.views import user_registration, user_logout

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('register/', user_registration, name='register'),
    path('logout/', user_logout, name='logout'),
]
