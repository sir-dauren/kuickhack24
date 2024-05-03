from typing import IO

from django.contrib.auth.models import User

from base.models import Document


def show_all_documents_service() -> list[Document]:
    """
        Получение всех документов
    """
    return Document.objects.all().order_by('-created')


def create_new_document_service(user: User, file, content: str):
    """
        Создание файлового документа

        :param user
        :param file
        :param content
        :return: Document object
    """
    return Document.objects.create(user=user,
                                   file=file,
                                   text=content)


def get_document_by_id_service(id: int, user_id: int) -> Document | None:
    """
        Получение документа по id

        :param user_id:
        :param id, user_id
        :return: Document object
    """
    try:
        document = Document.objects.get(id=id, user__id=user_id)
        return document
    except Document.DoesNotExist:
        return None


def delete_document_by_id_service(id: int, user_id: int) -> bool | None:
    """
        Удаление документа по id

        :param user_id:
        :param id, user_id
        :return: Document object
    """
    try:
        document = Document.objects.get(id=id, user__id=user_id)
        document.delete()
        return True
    except Document.DoesNotExist:
        return None
