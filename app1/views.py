from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Pessoa


class IndexView(ListView):
    models = Pessoa
    template_name = 'index.html'
    queryset = Pessoa.objects.all()
    context_object_name = 'pessoas'
    success_url = reverse_lazy('index')


class CreatePessoaView(CreateView):
    model = Pessoa
    template_name = 'pessoa_form.html'
    fields = ['nome', 'salario']
    success_url = reverse_lazy('index')


class UpdatePessoaView(UpdateView):
    model = Pessoa
    template_name = 'pessoa_form.html'
    fields = ['nome', 'salario']
    success_url = reverse_lazy('index')


class DeletePessoaView(DeleteView):
    model = Pessoa
    template_name = 'pessoa_del.html'
    success_url = reverse_lazy('index')
