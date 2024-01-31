from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    path('task-list/', views.taskList, name='api-overview'),
    path('task-detail/<str:pk>/', views.taskDetail, name='api-detail'),
    path('task-create/', views.taskCreate, name='api-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='api-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='api-delete'),
]