from rest_framework.serializers import CharField, ModelSerializer

from .models import User, City


class UserSerializer(ModelSerializer):
    """User serialiser."""

    class Meta:
        fields = (
            'id',
            'username',
            'city'
        )
        model = User
        extra_kwargs = {
            'username': {'required': True},
        }



class CitySerializer(ModelSerializer):
    """City serialiser."""

    class Meta:
        fields = (
            'id',
            'name',
            'is_primary'
        )
        model = City
