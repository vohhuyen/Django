# Generated by Django 5.1.2 on 2024-10-22 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanager', '0002_remove_employee_salary_delete_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-check_in'], 'permissions': [('can_edit_attendance', 'Can_edit_attendance'), ('can_delete_attendance', 'Can_delete_attendance')], 'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendances'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'permissions': [('can_edit_department', 'Can_edit_department'), ('can_delete_department', 'Can_delete_department')], 'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['user__username'], 'permissions': [('can_edit_employee', 'Can_edit_employee'), ('can_delete_employee', 'Can_delete_employee')], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'start_date'], 'permissions': [('can_edit_task', 'Can_edit_task'), ('can_delete_task', 'Can_delete_task')], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
