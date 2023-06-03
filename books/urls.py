from django.urls import path
from .views import BookListView
from rest_framework.authtoken import views

urlpatterns = [
    path('',BookListView.as_view(template_name = 'books/book_test.html')),
    path('api-token-auth/',views.obtain_auth_token),
]