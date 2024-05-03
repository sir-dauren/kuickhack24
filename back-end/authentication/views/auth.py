from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED
                                   )

from authentication.services.user_services import create_user_service, get_user_by_email_service, \
    get_user_by_username_service
from authentication.utils.authenticate_utils import check_user_password_util
from authentication.utils.token_generator_utils import access_refresh_tokens_generator, \
    access_token_remove_util


@api_view(['POST'])
def sign_up(request):
    """
        Регистрация нового пользователя
    """
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    password_confirmation = request.data['password_confirmation']

    if get_user_by_username_service(email):
        return Response({
           'message': 'Пользователь с таким именем уже существует'
        }, status=HTTP_400_BAD_REQUEST)

    if get_user_by_email_service(email):
        return Response({
           'message': 'Пользователь с такой почтой уже существует'
        }, status=HTTP_400_BAD_REQUEST)

    if password_confirmation != password:
        return Response({
            'message': 'Пароли не совпадают'
        }, status=HTTP_400_BAD_REQUEST)

    user = create_user_service(username, email, password)

    access_token = access_refresh_tokens_generator(user)

    return Response({
        'access_token': access_token,
    }, status=HTTP_201_CREATED)


@api_view(['POST'])
def sign_in(request):
    """
        Авторизация пользователя
    """
    email = request.data.get('email')
    password = request.data.get('password')

    user = get_user_by_email_service(email)

    if not user:
        return Response({
            'message': 'Пользователь не найден'
        }, status=HTTP_401_UNAUTHORIZED)

    if not check_user_password_util(password, user):
        return Response({
            'message': 'Пароль неверный'
        }, status=HTTP_401_UNAUTHORIZED)

    access_token = access_refresh_tokens_generator(user)

    return Response({
        'access_token': access_token,
    }, status=HTTP_200_OK)


@api_view(['POST'])
def sign_out(request):
    """
        Выход пользователя
    """
    authorization_header = request.headers.get('Authorization')
    if authorization_header and authorization_header.startswith('Bearer '):
        access_token = authorization_header.split(' ')[1]

        if access_token_remove_util(access_token):
            return Response({
                'message': 'Успешный выход из аккаунта'
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message': 'Токен неверный'
            }, status=HTTP_401_UNAUTHORIZED)
    else:
        return Response({
            'message': 'Токен не найден'
        }, status=HTTP_401_UNAUTHORIZED)
