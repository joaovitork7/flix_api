from rest_framework import serializers
from actors.models import actor


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = '__all__'
