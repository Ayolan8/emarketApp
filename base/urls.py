from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('addform/', views.addform, name='addform'),
    path('<int:id>/edit', views.editform, name='editform'),
    path('<int:id>/warning', views.delete_warning, name='warning'),
    path('d<int:id>/delete', views.delete_item, name='delete'),
]