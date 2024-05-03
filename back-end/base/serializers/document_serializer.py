from rest_framework.serializers import ModelSerializer
from base.models import Document


class DocumentSerializer(ModelSerializer):
    """
        Сериализатор для вывода документа
    """

    class Meta:
        model = Document
        fields = ('id', 'text', 'file', 'created')


