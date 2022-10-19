from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('birds/', views.birds_index, name='index'),
  path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
  path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
  path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='birds_update'),
  path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'),
  path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('shirts/', views.ShirtList.as_view(), name='shirts_index'),
  path('shirts/<int:pk>/', views.ShirtDetail.as_view(), name='shirts_detail'),
  path('shirts/create/', views.ShirtCreate.as_view(), name='shirts_create'),
  path('shirts/<int:pk>/update/', views.ShirtUpdate.as_view(), name='shirts_update'),
  path('shirts/<int:pk>/delete/', views.ShirtDelete.as_view(), name='shirts_delete'),
  path('birds/<int:bird_id>/assoc_shirt/<int:shirt_id>/', views.assoc_shirt, name='assoc_shirt'),
]