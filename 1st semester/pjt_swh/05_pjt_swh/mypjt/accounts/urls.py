from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'), # login
    path('logout/', views.logout, name='logout'), # logout
    path('signup/', views.signup, name='signup'), # signup
    path('update/', views.update, name='update'), # update
    path('delete/', views.delete, name='delete'), # delete
    path('password/', views.change_password, name='change_password'), # change_password
    # path('detail/', views.detail, name='detail'),
]