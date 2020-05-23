from rest_framework import mixins, viewsets


class CreateListUpdateViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
  pass