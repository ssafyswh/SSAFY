from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/thread_create/', views.thread_create, name='thread_create'),
    path('<int:thread_id>/thread_detail', views.thread_detail, name='thread_detail'),
    path('<int:thread_id>/thread_update', views.thread_update, name='thread_update'),
    path('<int:thread_id>/thread_delete', views.thread_delete, name='thread_delete'),
]
