"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo_list.views import TaskListView, TagListView, TaskCreateView, TagCreateView, TaskUpdateView, TaskDeleteView, \
    TaskUpdateDoneView, TagUpdateView, TagDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name="task-update"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),
    path('done/<int:pk>/', TaskUpdateDoneView.as_view(), name="task-update-done"),
    path('tags/', TagListView.as_view(), name="tag-list"),
    path('tags/create/', TagCreateView.as_view(), name="tag-create"),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name="tag-update"),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name="tag-delete"),

]
app_name = "todo-list"
