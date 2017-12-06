from libros.models import Libros
from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class LibroModelSerializer(serializers.ModelSerializer):
    # user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Libros
        fields = [
            'Nombre',
            'Autor',
            'Editorial',
            'ISBN',
            'Precio',
            'Creacion',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, obj):
        return obj.Creacion.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.Creacion) + "ago"
