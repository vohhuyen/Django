from rest_framework import permissions

class CanViewTask(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        employee = request.user.employee_profile
        return employee in obj.assigned_to.all() or request.user.is_superuser
