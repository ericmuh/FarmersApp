from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index),
    path('users/', include('Users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
