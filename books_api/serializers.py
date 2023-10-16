from django.contrib.auth.models import User, Group
from rest_framework import serializers
from books_api.models import Books  # Importe o modelo corretamente

# Define um serializador para o modelo User.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

# Define um serializador para o modelo Group.
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model = Group
        fields = ('url', 'name')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
