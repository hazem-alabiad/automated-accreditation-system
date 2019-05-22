from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView


# import views
from main.views import *

favicon_view = RedirectView.as_view(url='main/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', sign_in_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('create_admin/', create_admin_view, name='createAdmin'),
    path('/favicon.ico', favicon_view),

    #admin paths
    path('admin_homepage/', admin_home_page_view, name='adminHomePage'),
    path('admin_homepage/details/', entity_detail_view, name='adminEntityDetailsPage'),
    path('admin_homepage/add_entity/', add_entities_view, name='adminAddEntityPage'),
    path('admin_homepage/update_entity/', add_entities_view, name='adminUpdateEntityPage'),
    path('admin_homepage/delete_entity/', delete_entities_view, name='adminDeleteEntityPage'),

    #client paths
    path('client_homepage/', client_home_page_view, name='clientHomePage'),
    path('client_homepage/details/', entity_detail_view, name='clientEntityDetailsPage'),
    path('client_homepage/update_entity/', add_entities_view, name='clientUpdateEntityPage'),
    path('client_homepage/delete_entity/', delete_entities_view, name='clientDeleteEntityPage'),

    #common paths


]
