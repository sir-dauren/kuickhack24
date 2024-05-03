from django.contrib.auth.hashers import check_password


def check_user_password_util(password, user) -> bool:
    """
        Проверка пароля пользователя

        :param: password, user
        :return: bool
    """
    if check_password(password, user.password):
        return True
    return False
