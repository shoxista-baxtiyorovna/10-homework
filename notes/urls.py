from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('list/', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('detail/<int:note_id>/', views.note_detail, name='note_detail'),
    path('delete/<int:note_id>/', views.note_delete, name='note_delete'),
    path('update/<int:note_id>/', views.note_update, name='note_update'),
]