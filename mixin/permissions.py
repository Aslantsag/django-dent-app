from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin:

    def has_permission(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
