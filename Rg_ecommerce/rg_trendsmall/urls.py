from django.urls import path, include
from . import views
urlpatterns = [
    path ("", views.index, name = 'index'),
     path('currencies/', include('currencies.urls')),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),

    ] 