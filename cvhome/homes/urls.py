from django.urls import path
from . import views
app_name='homes'
urlpatterns = [
path('',views.viewcv, name='viewcv'),
path('admin/',views.viewhome, name='viewhome'),
path('<slug:slug>/',views.viewblog, name='viewblog'),
path('viewreadblog/<slug:slug>/',views.viewreadblog, name='viewreadblog'),






]