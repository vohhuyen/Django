# from django.urls import path
# from .views import (
#     DepartmentListView,
#     DepartmentCreateView,
#     DepartmentUpdateView,
#     DepartmentDeleteView,
#     DepartmentDetailView
# )
# from . import views


# urlpatterns = [
#     path('departments/', DepartmentListView.as_view(), name='department_list'),
#     path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
#     path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
#     path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
#     path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    
#     path('users/', views.UserListView.as_view(), name='user_list'),
#     path('users/create/', views.UserCreateView.as_view(), name='user_create'), 
#     path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'), 
#     path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'), 
#     path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
#     path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
#     path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'), 
#     path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'), 
#     path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'), 
#     path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),   
     
#     path('tasks/', views.list_tasks, name='list_tasks'), 
#     path('tasks/create/', views.create_task, name='create_task'), 
#     path('tasks/<int:pk>/', views.task_detail, name='task_detail'), 
#     path('tasks/update/<int:pk>/', views.edit_task, name='update_task'), 
#     path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
# ]


from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentDetailView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    UserListCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    EmployeeListCreateView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    TaskListCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    # Department URLs
    path('departments/', DepartmentListCreateView.as_view(), name='department_list_create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

    # User URLs
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),

    # Task URLs
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]

