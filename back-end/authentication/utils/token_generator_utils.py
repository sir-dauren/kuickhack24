from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from datetime import timedelta
from django.utils import timezone


def access_refresh_tokens_generator(user) -> {str, str}:
    """
        Генератор Access и Refresh токенов

        :param user:
        :return: Token
    """
    tokens = RefreshToken.for_user(user)
    # {str(tokens), str(tokens.access_token)}
    print(str(tokens), str(tokens.access_token))
    
    return str(tokens.access_token)


def access_token_remove_util(access_token) -> bool:
    """
        Проверка Access токена

        :param: access_token
        :return: bool
    """
    try:
        outstanding_token = OutstandingToken.objects.get(token=access_token)
        outstanding_token.blacklist()

        BlacklistedToken.objects.get_or_create(token=access_token)

        old_date = timezone.now() - timedelta(hours=24)
        BlacklistedToken.objects.filter(created__lt=old_date).delete()

        return True
    except:
        return False
