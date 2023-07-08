from django.urls import path
from . import views
urlpatterns = [
    path ("", views.index, name = 'index'),
    path ("products/<str:id>", views.singleproduct, name = 'singleproduct'),
    path ("laptops/<str:id>", views.singleproduct, name = 'singleproduct'),
    ]