from django.urls import path
from .views import IndexView, CreatePessoaView, UpdatePessoaView, DeletePessoaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('criar/', CreatePessoaView.as_view(), name='criar_pessoa'),
    path('<int:pk>/editar/', UpdatePessoaView.as_view(), name='editar_pessoa'),
    path('<int:pk>/delete/', DeletePessoaView.as_view(), name='deletar_pessoa'),
]
