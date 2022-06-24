from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('pagina/', views.pagina, name='pagina'),
    path('postagem/', views.postagem, name='postagem'),
    path('add/', views.add, name='add'),
    path('edit/<id>/', views.edit, name='edit'),
    path('edit_id/<id>/', views.edit_id, name='edit_id'),
    path('delete/<id>/', views.delete, name='delete'),
    path('lista/', views.lista, name='lista')
]
