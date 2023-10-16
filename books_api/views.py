from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from books_api.models import Books  # Importe o modelo corretamente
from books_api.serializers import UserSerializer, GroupSerializer, BooksSerializer

# Define uma API de visualização (viewset) para o modelo User
class UserBooks_APIView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Define uma API de visualização (viewset) para o modelo Group
class GroupBooks_APIView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  # Corrigindo "GroupSeralizer" para "GroupSerializer"
    permission_classes = [permissions.IsAuthenticated]

class BooksListAPIView(APIView):
    def get(self, request, format=None):
        books = Books.object.all()
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksAPIView(APIView):
    def get(self, request, pk, format=None):
        books = Books.objects.get(id=pk)
        serializer = BooksSerializer(books)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        books = Books.objects.get(id=pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        carro = Carros.objects.get(id=pk)
        serializer = BooksSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


