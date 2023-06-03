from rest_framework import pagination

#customize way of doing the pagination.
class CustomPagination(pagination.PageNumberPagination):
    page_size = 3 # it is a fixed parameter and rest are optional
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p' #we can use any name like in this case we use p if we want another name so we can use.
