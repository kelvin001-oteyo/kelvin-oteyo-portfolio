from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path("contact/", views.contact, name="contact"),

]
