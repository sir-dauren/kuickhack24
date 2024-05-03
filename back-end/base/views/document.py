from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)

from django.core.paginator import Paginator

from base.serializers.document_serializer import DocumentSerializer
from base.services.document_services import show_all_documents_service, create_new_document_service, \
    get_document_by_id_service, delete_document_by_id_service
from base.utils.pdf_extract_util import extract_text_from_pdf_util
from base.utils.text_handling_util import text_handling_util


@api_view(['GET'])
def document_list(request):
    """
        Получение всех документов
    """
    if request.user.is_authenticated:
        size = request.GET.get('size', 10)
        page_number = request.GET.get('page', 1)

        documents = show_all_documents_service()

        paginator = Paginator(documents, size)
        page_obj = paginator.get_page(page_number)

        return Response({
            'page': int(page_number),
            'size': int(size),
            'totalElements': len(documents),
            'content': DocumentSerializer(page_obj, many=True).data
        }, status=HTTP_200_OK)
    else:
        return Response({
           'message': 'Пользователь не авторизован'
        }, status=HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def document_create_file(request):
    """
        Создание нового документа
    """
    if request.user.is_authenticated:
        file = request.FILES['document']

        if not file:
            return Response({
               'message': 'Документ не найден'
            }, status=HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.pdf'):
            return Response({
                'message': 'Документ должен быть в формате PDF'
            }, status=HTTP_400_BAD_REQUEST)

        content = extract_text_from_pdf_util(file)

        text = text_handling_util(content)

        document = create_new_document_service(request.user, file, text)

        if document:
            return Response({
                'document': DocumentSerializer(document, many=False).data
            }, status=HTTP_201_CREATED)
        else:
            return Response({
               'message': 'Документ не создан'
            }, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'message': 'Пользователь не авторизован'
        }, status=HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
def document_delete_file(request, id: int):
    """
        Удаление документа по id
    """
    if request.user.is_authenticated:
        document = delete_document_by_id_service(id, request.user.id)

        if document:
            return Response({}, status=HTTP_204_NO_CONTENT)
        else:
            return Response({
               'message': 'Документ не найден'
            }, status=HTTP_404_NOT_FOUND)
    else:
        return Response({
            'message': 'Пользователь не авторизован'
        }, status=HTTP_401_UNAUTHORIZED)