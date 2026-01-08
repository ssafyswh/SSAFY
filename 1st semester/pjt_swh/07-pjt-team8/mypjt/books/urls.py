from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views

app_name = 'books'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    # path('<int:id>/update', views.update, name='update'),
    # path('<int:id>/delete', views.delete, name='delete'),
    # path('<int:id>/thread_create/', views.thread_create, name='thread_create'),
    # path('<int:thread_id>/thread_detail', views.thread_detail, name='thread_detail'),
    # path('<int:thread_id>/thread_update', views.thread_update, name='thread_update'),
    # path('<int:thread_id>/thread_delete', views.thread_delete, name='thread_delete'),
    path('', views.book_list),
    path('<int:book_pk>/', views.book_detail),
    path('categories/', views.category_list),
    path('threads/', views.thread_list),
    path('threads/<int:thread_pk>/', views.thread_detail),
    path('<int:book_pk>/threads/', views.create_thread),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
