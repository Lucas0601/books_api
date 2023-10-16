from django.urls import path

from books_api.views import BooksListAPIView, BooksAPIView

urlpatterns = [
    path('books/', BooksListAPIView.as_view(), name='books_list_create'),
    path('books/<int:pk>', BooksAPIView.as_view(), name='books_retrieve_update_destroy'),
]