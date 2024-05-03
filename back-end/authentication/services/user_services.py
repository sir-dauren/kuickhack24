from typing import Any

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def create_user_service(username: str, email: str, password: str) -> User:
    """
        Создание нового пользователя

        :param: username, email, password
        :return: User object
    """
    return User.objects.create(
        username=username,
        email=email,
        password=make_password(password))


def get_user_by_email_service(email: str) -> User | None:
    """
        Взятие пользователя по email

        :param: email
        :return: User object
    """
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def get_user_by_username_service(username: str) -> User | None:
    """
        Взятие пользователя по username

        :param: username
        :return: User object
    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def update_user_service(user, username, email) -> User:
    """
        Обновление пользователя

        :param: username, email
        :return: User object
    """
    try:
        user.username = username
        user.email = email
        user.save()
        return user
    except User.DoesNotExist:
        return None