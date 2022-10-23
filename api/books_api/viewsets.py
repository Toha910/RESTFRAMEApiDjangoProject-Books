from rest_framework import viewsets
from api.models import Book
from api.books_api.serializers import BookSerializer
# import permissions
# from rest_framework import permissions, authentication

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all() # queryset for this viewset
    # permission_classes = [permissions.IsAdminUser]
    # authentication_classes = [authentication.TokenAuthentication]
