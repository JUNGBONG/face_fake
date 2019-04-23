from django.urls import path
from . import views
app_name = 'asdf'
urlpatterns=[
    path("", views.list, name='lalala'),
    path("create/", views.create),
    path("<int:id>/delete/",views.delete, name='delete'),
    path("<int:idid>/edit/",views.edit, name='edit'),
    ]