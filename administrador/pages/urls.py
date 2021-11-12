from django.urls import path
from .views import PageListView , PageDetailView, PageCreate, PageDelete, PageUpdate, busquedaList
from .views import PredioListView, PredioDetailView, PredioCreate, PredioDelete, PredioUpdate
from .views import PropietarioCreate, PropietarioDetailView, PropietarioDelete, PropietarioListView, PropietarioUpdate
pages_patterns = ([
    #URls lista
    path('', PageListView.as_view(), name='pages'),
    path('lista/propietarios/', PropietarioListView.as_view(), name='propietarios'),
    path('lista/predios/', PredioListView.as_view(), name='predios'),

    #URl detalle
    path('page/<int:pk>/', PageDetailView.as_view(), name='page'),
    path('propietario/<int:pk>/', PropietarioDetailView.as_view(), name='propietario'),
    path('predio/<int:pk>/', PredioDetailView.as_view(), name='predio'),


    #URL para formularios
    path('create/', PageCreate.as_view(), name='create'),
    path('propietario/', PropietarioCreate.as_view(), name='propietarioCreate'),
    path('predio/', PredioCreate.as_view(), name='predioCreate'),

    #URL para actualizar
    path('update/matricula/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('update/propietario/<int:pk>/', PropietarioUpdate.as_view(), name='propietarioUpdate'),
    path('update/predio/<int:pk>/', PredioUpdate.as_view(), name='predioUpdate'),

    #URL para borrar
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('delete/propietario/<int:pk>/', PropietarioDelete.as_view(), name='propietarioDelete'),
    path('delete/predio/<int:pk>/', PredioDelete.as_view(), name='predioDelete'),

], 'pages')