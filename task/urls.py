from django.conf.urls import url
from django.urls import path

from task import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'status/create', views.createStatus, name='status-create'),
    url(r'status/list', views.listStatus, name='status-list'),
    url(r'status/save', views.persistenceStatus, name='status-save'),
    path(r'status/destroy/<int:id>', views.destroyStatus, name='status-destroy'),

    url(r'task/create', views.createTask, name='task-create'),
    url(r'task/save', views.persistenceTask, name='task-save'),
    url(r'task/list', views.home, name='task-list'),
    path(r'task/destroy/<int:id>', views.destroyTask, name='task-destroy'),
    path(r'task/update/<int:id>', views.editTask, name='task-edit'),


    url(r'user/create', views.createUser, name='user-create'),
    url(r'user/save', views.persistenceUser, name='user-save'),
]
