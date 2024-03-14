# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, evonPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('evon/', evonPageView, name='evon'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/<str:gmat>', results, name='results'),

]
