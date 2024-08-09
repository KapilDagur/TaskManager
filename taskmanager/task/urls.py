from django.urls import path
from .views import (
    TaskListView, 
    TaskDetailView, 
    TaskCreateView, 
    TaskUpdateView, 
    TaskDeleteView, 
    TaskListCreateAPIView, 
    TaskRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    #DJANGO VIEW
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<uuid:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<uuid:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<uuid:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    #API VIEW
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create-api'),
    path('api/tasks/<uuid:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-rud-api'),
]
