from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
# from authentication.serializers.profile_serializers import ProfileSerializer


class UserSerializer(ModelSerializer):
    """
        Сериализатор для пользователя
    """

    # profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('username', 'email',)
