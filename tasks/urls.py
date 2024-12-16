from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
]