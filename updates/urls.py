from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpdateListView.as_view(), name='update_list'),
    path('<slug:slug>/', views.UpdateDetailView.as_view(), name='update_detail'),
    path('blog/<slug:slug>/', views.update_detail, name='update_detail'),

]
