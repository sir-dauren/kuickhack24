from rest_framework.serializers import ModelSerializer
from authentication.models import Profile
from authentication.serializers.user_serializers import UserSerializer


class ProfileSerializer(ModelSerializer):
    """
        Сериализатор для профиля
    """
    # user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('image', )
