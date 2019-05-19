from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView


# import views
from main.views import sign_in_view, admin_home_page_view, create_admin_view, client_home_page_view

favicon_view = RedirectView.as_view(url='main/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', sign_in_view, name='signin'),
    path('create_admin/', create_admin_view, name='createAdmin'),
    path('/favicon.ico', favicon_view),

    #admin paths
    path('admin_homepage/', admin_home_page_view, name='adminHomePage'),



    #client paths
    path('client_homepage/', client_home_page_view, name='clientHomePage'),
]
