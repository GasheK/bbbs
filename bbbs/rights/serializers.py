from rest_framework import serializers

from bbbs.rights.models import Right

class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = "__all__"
