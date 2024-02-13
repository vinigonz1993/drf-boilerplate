from rest_framework.serializers import Serializer


class UserSerializer(Serializer):

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "username": instance.username,
        }
