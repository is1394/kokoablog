from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^new', views.new_entry, name='crear_entrada'),
    url(r'^edit/(?P<id_entry>\d+)/$',views.edit_entry, name='editar_entrada'),
    url(r'^delete/(?P<id_entry>\d+)/$',views.del_entry, name='eliminar_entrada'),



    url(r'class/list', views.EntryList.as_view()),
    url(r'class/new', views.EntryCreate.as_view()),
    url(r'^class/edit/(?P<pk>\d+)/$',views.EntryUpdate.as_view()),
    url(r'^class/delete/(?P<pk>\d+)/$',views.EntryDelete.as_view()),


]
