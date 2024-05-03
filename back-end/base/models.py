import uuid

from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    """
        Документ пользователя
    """

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def document_directory_path(instance, filename):
        """
            Функция для определения пути для сохранения файла документа
        """
        username = instance.user.username if instance.user else 'unknown_user'
        extension = filename.split('.')[-1]
        new_filename = f'{username}_document_{uuid.uuid4().hex[:10]}.{extension}'

        return f'uploads/users/{username}/documents/{new_filename}'

    file = models.FileField(upload_to=document_directory_path,
                            blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def text_document(cls, text) -> object:
        return Document.objects.create(
            text=text,
        )

    @classmethod
    def file_document(cls, file) -> object:
        return Document.objects.create(
            file=file,
        )

    def __str__(self) -> str:
        return self.text if self.text else self.file.name