from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Профиль пользователя
    """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    def user_directory_path(self, filename):
        return f'uploads/users/{self.user.username}/avatars/'

    image = models.ImageField(upload_to=user_directory_path,
                              blank=True)

    def __str__(self) -> str:
        return self.user.username
