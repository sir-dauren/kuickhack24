from django.urls import path
from base.views import document

urlpatterns = [
    path('documents/', document.document_list, name='document-list'),
    path('documents/create/', document.document_create_file, name='document-create-file'),
    path('documents/<int:id>/', document.document_delete_file, name='document-delete-file'),
]
