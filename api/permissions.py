from rest_framework import permissions

OWNER_ACTIONS = ('update', 'partial_update', 'destroy')
OWNER_UPDATE_ACTIONS = ('update', 'partial_update')

class ObjectOwnerPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    return True

  def has_object_permission(self, request, view, obj):
    return obj.user == request.user

def get_permissions(action, acceptable_actions):
  if action in acceptable_actions:
    return [permissions.IsAuthenticated(), ObjectOwnerPermission()]
  return [permissions.IsAuthenticated()]
