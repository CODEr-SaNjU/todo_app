from django.urls import path,include
from main_app.views import TaskListCreateView, TaskRretrieveUpdateDeleteView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskRretrieveUpdateDeleteView.as_view(), name="task-retrieve-update-delete"),
]