"""
URL configuration for estoque_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from estoque import views
from estoque.views import lista_estoque, adicionar_item, detalhes_item, editar_item, verificar_exclusao


urlpatterns = [
    path('', views.lista_estoque, name='lista_estoque'),
    path('adicionar/', views.adicionar_item, name='adicionar_item'),
    path('<int:id>/', views.detalhes_item, name='detalhes_item'),
    path('<int:id>/editar/', views.editar_item, name='editar_item'),
    path('<int:id>/excluir/', views.verificar_exclusao, name='verificar_exclusao'),
]