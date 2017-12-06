from rest_framework import generics, permissions

from django.db.models import Q
from libros.models import Libros
from .serializers import LibroModelSerializer
from .pagination import StandarResultPagination


class LibrosCreateAPIView(generics.CreateAPIView):
    serializer_class = LibroModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        serializer.save()


class LibrosListAPIView(generics.ListAPIView):
    serializer_class = LibroModelSerializer
    pagination_class = StandarResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Libros.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(Autor__icontains=query) | Q(Nombre__icontains=query)
            )
        return qs
