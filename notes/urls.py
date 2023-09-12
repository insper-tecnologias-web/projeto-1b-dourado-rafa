from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete_note, name='delete'),
    path('edit/<int:id>/',   views.edit_note, name='edit'),
    path('update/<int:id>/',  views.update_note, name='update'),
]