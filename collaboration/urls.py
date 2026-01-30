from django.urls import path
from .views import collaborate, dashboard

urlpatterns = [
    path('', collaborate, name='collaborate'),
    path('dashboard/', dashboard, name='collab_dashboard'),
]