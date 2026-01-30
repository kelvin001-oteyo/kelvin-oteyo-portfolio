from django.contrib import admin
from django.urls import path, include
from core.views import home, skills,education

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('core.urls')),
    path('skills/', skills, name='skills'),
    path('projects/', include('projects.urls')),
    path('education/', education, name='education'),
    path('updates/', include('updates.urls')),
    path('accounts/', include('accounts.urls')),
    path('collaboration/', include('collaboration.urls')),
    


]
