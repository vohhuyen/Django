import json
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from staffmanager.models import Task 
import os 
from django.conf import settings
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Load initial data from initial_data.json and create permissions'
   
    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'staffmanager/fixtures/initial_data.json')
        with open(file_path) as f:
            data = json.load(f)

        for user_data in data:
            if user_data['model'] == 'auth.user':
                user_data['fields']['password'] = make_password(user_data['fields']['password'])
                User.objects.update_or_create(
                    username=user_data['fields']['username'],
                    defaults=user_data['fields']
                )
        
        # call_command('loaddata', 'tasks.json') 

        for task in Task.objects.all():
            content_type = ContentType.objects.get_for_model(Task)
            permissions = [
                f'can_view_task_{task.id}',
                f'can_edit_task_{task.id}',
                f'can_delete_task_{task.id}',
            ]
            
            for perm in permissions:
                Permission.objects.get_or_create(
                    codename=perm,
                    name=f'Can {perm.replace("_", " ")}',
                    content_type=content_type,
                )

            try:
                superadmin = User.objects.get(username='superadmin')
                for perm in permissions:
                    permission = Permission.objects.get(codename=perm, content_type=content_type)
                    superadmin.user_permissions.add(permission)
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING('Superadmin user does not exist.'))

        self.stdout.write(self.style.SUCCESS('Initial data loaded and permissions created successfully.'))