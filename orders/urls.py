from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groupbuy/<int:id>/', views.groupbuy_detail, name='groupbuy_detail'),
    path('register/', views.register, name='register'),
    path('create/', views.create_groupbuy, name='create_groupbuy'),
    path('groupbuy/delete/<int:id>/', views.delete_groupbuy, name='delete_groupbuy'),
]