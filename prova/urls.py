from django.urls import path
from . import views


urlpatterns = [
  path('', views.home),
  path('produto/', views.produto_list),
  path('produto/<int:produto_id/>', views.produto_show),
  path('produto/create/', views.produto_form ),
  path('editar/<int:produto_id/>', views.produto_editar),
  path('excluir/<int:produto_id/>', views.produto_excluir)
]