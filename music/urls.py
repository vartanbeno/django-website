from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # /music/<album_id>
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]