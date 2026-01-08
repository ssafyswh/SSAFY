from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
  path('create/', views.create, name='create'), # todo: 게시글 작성  ( /create/ )
  path("", views.index, name='index'), # todo: 게시글 전체 조회  ( / )
  # path('/<int:id>/', views.detail, name='detail')# todo: 게시글 상세 조회  ( /<int:id>/ )
  # todo: 게시글 수정  ( /<int:id>/update/ )
  # todo: 게시글 삭제  ( /<int:id>/delete/ )
]
