from .views import FileView,FileAllView
from django.urls import path

urlpatterns = [
    path('upload_file/', FileView.as_view(), name='file_upload'),
    path('file_all_data/',FileAllView.as_view(), name='file_all_data'),
]