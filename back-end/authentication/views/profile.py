from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED
                                   )

from authentication.serializers.user_serializers import UserSerializer
from authentication.services.user_services import update_user_service


@api_view(['GET', 'POST'])
def profile(request):
    if request.user.is_authenticated:
        """
            Показ профиля
        """
        if request.method == 'GET':
            user = request.user

            if user:
                return Response({
                    'user': UserSerializer(user, many=False).data
                }, status=HTTP_200_OK)

        """
            Обновление профиля
        """
        if request.method == 'POST':
            username = request.data.get('username')
            email = request.data.get('email')

            if username is None or email is None:
                return Response({
                    'message': 'Имя пользователя или почта не правильные'
                }, status=HTTP_400_BAD_REQUEST)

            update_user_service(user, username, email)

            return Response({
                'user': UserSerializer(user, many=False).data
            }, status=HTTP_200_OK)
    else:
        return Response({
            'message': 'Пользователь не авторизован'
        }, status=HTTP_401_UNAUTHORIZED)
