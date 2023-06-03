from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer,IndividualSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .page_number_pagination import CustomPagination

# Create your views here.

#To fetch all the records from the table.
class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    pagination_class = CustomPagination #for pagination

#To fetch the individual data from the table.
class BookDetailView(generics.RetrieveAPIView):
    #Line number 20 and 21 is for creating a authentication for the page.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = IndividualSerializer #It give individual records
    # serializer_class = BookSerializer #It gives all the records from the table  


#Customize way of pushing data using rest API
class CreateAPIView(APIView):
    def post(self, request): #agar method ke andar hum format=None to iska kaam hai ki konse format me data rahega.
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_401_BAD_REQUEST)
    

#Customize Updating the data using rest API
class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


#Custom Delete Api 
class DeleteBookAPIView(APIView):
    def delete(self, request,id = None):
        book_data = Book.objects.filter(id=id)
        book_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#another way to delete using generics
# class BookDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookSerializer
#     lookup_url_kwarg = 'id'
#     queryset = Book.objects.all()