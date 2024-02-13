from rest_framework.serializers import Serializer


class UserSerializer(Serializer):

    def to_representation(self, instance):
        return {
            "username": instance.username,
            "id": instance.username
        }
