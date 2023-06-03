from django.urls import path
from .views import BookListApi,BookDetailView,CreateAPIView,BookUpdateView,DeleteBookAPIView

urlpatterns = [
    path('',BookListApi.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', CreateAPIView.as_view(), name='create_api'),
    path('update_book/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('book-delete/<int:id>/',DeleteBookAPIView.as_view(), name='book-delete'),


]