from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView


# import views
from main.views import sign_in_view, admin_home_page_view, create_admin_view, client_home_page_view, entity_detail_view, signout_view, add_entities_view

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

    #client paths
    path('client_homepage/', client_home_page_view, name='clientHomePage'),
    path('client_homepage/details/', entity_detail_view, name='clientEntityDetailsPage'),
    path('client_homepage/add_entity/', add_entities_view, name='clientAddEntityPage'),

    #common paths


]
