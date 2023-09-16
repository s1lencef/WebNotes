from django.urls import path,include
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_window, name = 'home'),
    path('registration/', include('registration.urls')),
    path('todo/', views.todo_window, name = 'todo'),
    path('change-task/<int:id>/<str:status>/<int:type>', views.change_task_status, name ='change-task-status'),
    path('delete/<int:type>/<int:id>', views.delete_tasks, name ='delete'),
    path('task-manager/', views.task_manager_window, name='manager'),
    path('task-manager/add-task', views.add_task_window, name = 'add_task'),
    path('task-manager/add-task/<int:id>', views.inter_task_window, name = 'int_task'),
    path('task-manager/edit-task/<int:id>', views.edit_task_window, name = 'edit_task'),
]