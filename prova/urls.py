from django.urls import path
from . import views


urlpatterns = [
  path('', views.home),
  path('produto/', views.produto_list),
  path('produto/<int:produto_id>/', views.produto_show),
  path('produto/create', views.produto_form )
]