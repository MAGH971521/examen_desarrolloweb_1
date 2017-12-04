from django.contrib.auth import get_user_model
from rest_framework import serializers


class LibroModelSerializer(serializers.ModelSerializer):
    def get_date_display(self):
        pass

    def get_timesince(self):
        pass
