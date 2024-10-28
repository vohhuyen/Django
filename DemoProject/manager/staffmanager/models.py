from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = self.object.employees.select_related('user')
        return context

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['name']


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['user__username']

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)
    work_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.employee.user.username} - {self.check_in.date()}'

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        ordering = ['-check_in']


class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=100)  
    description = models.TextField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='tasks') 
    assigned_to = models.ManyToManyField(Employee, related_name='assigned_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.employee.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        content_type = ContentType.objects.get_for_model(Task)
        for employee in self.assigned_to.all():
            view_permission, created = Permission.objects.get_or_create(
                codename=f'can_view_task_{self.id}',
                defaults={'name': f'Can view task {self.title}', 'content_type': content_type}
            )
            edit_permission, created = Permission.objects.get_or_create(
                codename=f'can_edit_task_{self.id}',
                defaults={'name': f'Can edit task {self.title}', 'content_type': content_type}
            )
            delete_permission, created = Permission.objects.get_or_create(
                codename=f'can_delete_task_{self.id}',
                defaults={'name': f'Can delete task {self.title}', 'content_type': content_type}
            )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['status', 'start_date']