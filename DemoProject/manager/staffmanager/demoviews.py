from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Department, Employee, Task
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import CustomUserCreationForm, UserForm, EmployeeForm, TaskForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

class DepartmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Department
    template_name = 'departments/department_list.html'
    context_object_name = 'departments'
    permission_required = 'staffmanager.view_department'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class DepartmentCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Department
    fields = ['name', 'description']
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('department_list')
    permission_required = 'staffmanager.add_department'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class DepartmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Department
    fields = ['name', 'description']
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('department_list')
    permission_required = 'staffmanager.change_department'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class DepartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Department
    template_name = 'departments/department_confirm_delete.html'
    success_url = reverse_lazy('department_list')
    permission_required = 'staffmanager.delete_department'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class DepartmentDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Department
    template_name = 'departments/department_detail.html'
    context_object_name = 'department'
    permission_required = 'staffmanager.view_department'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')



class UserListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    permission_required = 'staffmanager.view_user'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')
    

class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
    permission_required = 'staffmanager.view_user'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'staffmanager.add_user'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'staffmanager.change_user'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    permission_required = 'staffmanager.delete_user'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')


class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    permission_required = 'staffmanager.view_employee'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'
    permission_required = 'staffmanager.view_employee'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'staffmanager.add_employee'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')
    def form_valid(self, form):
        user = User.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )
        employee = form.save(commit=False)
        employee.user = user 
        return super().form_valid(form)

class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'staffmanager.change_employee'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')

class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'staffmanager.delete_employee'
    def handle_no_permission(self):
        return render(self.request, 'errors/403.html')
    
    
    
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            print("employee_profile",  request.user.employee_profile)
            view_permission = Permission.objects.get(codename=f'can_view_task_{task.id}')
            edit_permission = Permission.objects.get(codename=f'can_edit_task_{task.id}')
            task.employee.user.user_permissions.add(view_permission, edit_permission)
            
            return redirect('task_detail', pk=task.id)
    else:
        form = TaskForm()
    
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if not request.user.has_perm(f'staffmanager.can_edit_task_{task.id}'):
        return render(request, 'errors/403.html') 
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    if not request.user.has_perm(f'staffmanager.can_view_task_{task.id}'):
        return render(request, 'errors/403.html') 
    
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if not request.user.has_perm(f'staffmanager.can_edit_task_{task.id}'): 
        return render(request, 'errors/403.html')  
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'tasks/delete_task.html', {'task': task})


@login_required
def list_tasks(request):
    tasks = Task.objects.all()
    viewable_tasks = []
    for task in tasks:
        if request.user.has_perm(f'staffmanager.can_view_task_{task.id}'):
            viewable_tasks.append(task)
    
    return render(request, 'tasks/list_tasks.html', {'tasks': viewable_tasks})
