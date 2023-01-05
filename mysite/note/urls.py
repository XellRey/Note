from django.urls import path
from . import views

app_name = 'note'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views. detail, name='detail')
]
