from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from schoolapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('users/', include('users.urls', namespace='users')),
    path('map/', views.map_view, name='map'),
    path('gemini/', views.gemini_view, name='gemini'),   # ← AJOUTER CETTE LIGNE
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)