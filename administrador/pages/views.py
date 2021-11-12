from django.http.response import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pages.form import PropietarioForm
from pages.models import Matricula, Predio, Propietario
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q


# Create your views here. 
def busquedaList(request):
    busqueda = request.GET.get('buscar')
    matricula = Matricula.objects.all()
    #data_propietario = Propietario.objects.filter(id_propietario = id )

    if busqueda:
        matricula = Matricula.objects.filter(
            Q(propietario__icontains = busqueda)|
            Q(predio__icontains = busqueda)
        ).distinct()

    return render(request, 'matricula_list.html', {'matricula':matricula})


#CRUD matricula
#Lista
class PageListView(ListView):
    model = Matricula
    queryset = Matricula.objects.order_by('-id')
    paginate_by = 5


#Detalle
class PageDetailView(DetailView):
    model = Matricula


#fromulario
class PageCreate(CreateView):
    model = Matricula
    fields = "__all__"
    success_url = reverse_lazy('pages:pages')

#Actualizar
class PageUpdate(UpdateView):
    model = Matricula
    fields = ['propietario', 'predio']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:update')

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

#Borrar
class PageDelete(DeleteView):
    model = Matricula
    success_url = reverse_lazy('pages:pages')


#CRUD propietario
#Lista
class PropietarioListView(ListView):
    model = Propietario
    queryset = Propietario.objects.order_by('-id')
    paginate_by = 5


#Detalle
class PropietarioDetailView(DetailView):
    model = Propietario

#fromulario
class PropietarioCreate(CreateView):
    model = Propietario
    form_class = PropietarioForm
    success_url = reverse_lazy('pages:create')

    def get_form(self, form_class=None):
        form = super(PropietarioCreate, self).get_form()
        #Modificar en tiempo real
        form.fields['nombre'].widget = forms.TextInput(attrs={'placeholder':'Nombre'})
        form.fields['identificacion'].widget = forms.TextInput(attrs={'placeholder':'Identificación'})

        return form


class PropietarioUpdate(UpdateView):
    model = Propietario
    fields = ['nombre', 'identificacion']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:propietarioUpdate', args=[self.object.id]) + '?ok'

class PropietarioDelete(DeleteView):
    model = Propietario
    success_url = reverse_lazy('pages:propietarios')

#CRUD predio
#Lista
class PredioListView(ListView):
    model = Predio
    paginate_by = 5

    def filter_urbano():
        pass

#Detalle
class PredioDetailView(DetailView):
    model = Predio

#Fromulario
class PredioCreate(CreateView):
    model = Predio
    fields = "__all__"
    success_url = reverse_lazy('pages:create')

#Actualizar
class PredioUpdate(UpdateView):
    model = Predio
    fields = ['cedula_catastral', 'direccion', 'tipo']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:predioUpdate', args=[self.object.id]) + '?ok'

#Borrar
class PredioDelete(DeleteView):
    model = Predio
    success_url = reverse_lazy('pages:predios')