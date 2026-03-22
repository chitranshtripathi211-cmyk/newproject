from django.urls import path
from . import views

urlpatterns = [
    #dashboard
    path('', views.dashboard, name='dashboard'),
    # add item
    path('add/', views.add_item, name='add_item'),

    # auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # edit delete
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),

]