from libros.models import Libros
from rest_framework import serializers
from django.utils.timesince import timesince


class LibroModelSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Libros
        fields = [
            'Nombre',
            'Autor',
            'Editorial',
            'Sinopsis',
            'Creacion',
            'date_display',
            'timesince',
            'id'
        ]

    def get_date_display(self, obj):
        return obj.Creacion.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.Creacion) + "ago"
