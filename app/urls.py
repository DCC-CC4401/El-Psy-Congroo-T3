from django.conf.urls import url

from app import views

urlpatterns = [
    #/app/
    url(r'^$', views.index, name='index'),
    #/app/login
    url(r'^login$', views.login, name='login'),
    #/app/signup
    url(r'^register$', views.register, name='register'),
    #/app/vendedor
    url(r'^vendedor$', views.vendedorprofilepage, name='vendedorprofilepage'),
    #/app/productos
    url(r'^productos$', views.gestionproductos, name='gestionproductos'),
    #/app/usuario
    url(r'^usuario$', views.profile_edit, name='profile_edit'),
    # /app/register2
    url(r'^register2$', views.register2, name='register2'),
    # /app/productos2
    url(r'^productos2$', views.productos2, name='productos2'),
]