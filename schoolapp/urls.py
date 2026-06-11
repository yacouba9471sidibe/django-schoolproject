from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('map/', views.map_view, name='map'),
]