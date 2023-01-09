from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.note, name='note'),
    path('<int:pk>/edit/', views.edit.as_view(), name='edit'),
    path('<int:pk>/delete/', views.delete.as_view(), name='delete')

]
