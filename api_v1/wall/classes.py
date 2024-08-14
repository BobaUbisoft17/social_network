from rest_framework import mixins, viewsets


class MixedPermission:
    """Миксин permissions для action"""

    def get_permissions(self):
        """Нужно переделать"""
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CreateRetrieveUpdateDestroy(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    MixedPermission,
    viewsets.GenericViewSet,
):
    pass


class CreateUpdateDestroy(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    MixedPermission,
    viewsets.GenericViewSet,
):
    pass
